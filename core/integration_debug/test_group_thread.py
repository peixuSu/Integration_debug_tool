#!/usr/bin/env python3.13
"""
filename: test_group_thread.py
author: [spx]
email: [3123002434@mail2.gdut.edu.cn]
date: 2025-12-15
description: 测试数据组线程类，用于处理测试数据组操作
"""

from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import QThread, Signal, QElapsedTimer, Qt

class SendModeThread(QThread):
    """
    数据发送工作线程类
    
    该类继承自QThread，提供了多线程的数据发送功能，支持多种发送模式。
    通过信号机制与UI线程通信，报告发送状态和日志信息。
    
    Signals:
        finished_signal (): 线程完成信号
        log_signal (str): 日志发送信号
    """
    
    finished_signal = Signal()
    log_signal = Signal(str)

    # ==================== 初始化功能 ====================
    def __init__(self, application,spi_controller):
        """
        初始化SendModeThread实例
        
        Args:
            application: 主应用程序实例
        """
        super().__init__()
        self.application = application
        self.ui = self.application.ui
        self.spi_controller = spi_controller
        self.running = False

    # ==================== 参数设置功能 ====================
    def set_params(self, delay, items, mode, cycles='', times=1, is_single_group=False):
        """
        设置发送参数
        
        Args:
            delay (float): 发送间隔延迟（秒）
            items (list): 要发送的数据项列表
            mode (str): 发送模式 ("circ")
            cycles (int/str): 循环次数，仅在循环模式下使用
            times (int): 随机发送次数，仅在随机模式下使用
            is_single_group (bool): 是否为单组发送模式
        """
        self.delay = delay
        self.items = items
        self.mode = mode
        self.cycles = cycles
        self.times = times
        self.is_single_group = is_single_group

    # ==================== 延迟控制功能 ====================
    def delay_fuction(self, seconds):
        """
        延迟函数
        
        提供高精度的延迟控制，确保发送间隔的准确性。
        
        Args:
            seconds (float): 延迟时间（秒）
        """
        timer = QElapsedTimer()
        timer.start()

        target_ms = int(seconds * 1000)

        while self.running and timer.elapsed() < target_ms:
            remaining = target_ms - timer.elapsed()

            if remaining > 10:
                self.msleep(10)
            elif remaining > 1:
                self.msleep(1)

    # ==================== 发送模式功能 ====================
    def send_cyclic(self):
        """
        循环发送数据
        
        支持指定循环次数或持续发送直到手动停止。
        在每次循环之间插入用户设定的延迟。
        """
        # # 添加调试信息
        # self.log_signal.emit(f"开始循环发送，数据项数量: {len(self.items)}", 0)
        
        if self.is_single_group is True:
            # 单组模式下，只发送当前选中的组
            self.send_poll(self.items, cyclic_mode=False)
                # 在延迟之前检查是否需要停止
            if not self.running:
                return

            # 检查SPI设备是否仍然连接
            if self.spi_controller.driver.dev_handle is None:
                self.running = False
                return

            if not self.running:
                return
            
            # 添加调试信息，显示当前发送的组名
            group_name, _ = self.items[0].data(Qt.UserRole)
            self.log_signal.emit(f"发送组: {group_name}")
            return
        else:
            # 当未指定循环次数时，持续发送直到手动停止
            if not self.cycles:
                cycle_count = 0
                while self.running:
                    cycle_count += 1
                    
                    self.send_poll(self.items, cyclic_mode=True)
                    # 在延迟之前检查是否需要停止
                    if not self.running:
                        break

                    # 检查SPI设备是否仍然连接
                    if self.spi_controller.driver.dev_handle is None:
                        self.running = False
                        return

                    if not self.running:
                        break

                    # 添加调试信息，显示当前循环次数
                    self.log_signal.emit(f"完成第{cycle_count}次循环")
                    self.delay_fuction(self.delay)
                return
            
            # 指定循环次数的发送
            # self.log_signal.emit(f"开始指定次数循环发送，循环次数: {self.cycles}")
            for i in range(self.cycles):
                # 在每次循环开始前检查是否需要停止
                if not self.running:
                    break

                # self.log_signal.emit(f"开始第{i+1}次循环")

                self.send_poll(self.items, cyclic_mode=True)
                # 在延迟之前检查是否需要停止
                if not self.running:
                    break
                if i < (self.cycles - 1) and self.delay > 0:
                    self.delay_fuction(self.delay)
                
                # 检查SPI设备是否仍然连接
                if self.spi_controller.driver.dev_handle is None:
                    self.running = False
                    return
                
                # 在发出进度信号前再次检查是否需要停止
                if not self.running:
                    break

                # 添加调试信息，显示当前循环和总循环次数
                self.log_signal.emit(f"完成第{i+1}次循环，总共{self.cycles}次")

    def send_poll(self, items, cyclic_mode=False):
        """
        轮询发送数据组
        
        按顺序发送每个数据组内的所有数据项，在组内数据项之间使用固定延迟，
        在数据组之间使用用户设定的延迟。
        
        Args:
            items (list): 数据组列表
            cyclic_mode (bool): 是否处于循环模式
        """
        # # 添加调试信息
        # self.log_signal.emit(f"开始轮询发送，数据项数量: {len(items)}, 循环模式: {cyclic_mode}", 0)
        
        # 检查SPI设备是否仍然连接
        if self.spi_controller.driver.dev_handle is None:
            # 设备已断开，停止发送
            self.running = False
            self.log_signal.emit("SPI设备已断开，停止发送")
            self.ui.button_start.setEnabled(True)
            self.ui.button_stop.setEnabled(False)
            return

        current_group_name = None
        
        for i, item in enumerate(items):
            # 在每次发送前检查是否需要停止
            if not self.running:
                return

            op_timer = QElapsedTimer()
            op_timer.start()

            # 检查数据项是否包含组名信息
            data_tuple = item.data(Qt.UserRole)
        
            # 包含组名信息的数据项
            group_name, actual_data = data_tuple

            # print(f"group_name: {group_name}, actual_data: {actual_data}")
            
            # 检查是否是新组（第一次遇到该组或组名变化）
            is_new_group = (current_group_name is None) or (current_group_name != group_name)
            
            # 如果是新组且处于循环模式，发送进度信号（表示前一个组发送完成）
            if current_group_name is not None and is_new_group and cyclic_mode is True:
                if self.spi_controller.driver.dev_handle is None:
                    self.running = False
                    return
                # 在发出进度信号前检查是否需要停止
                if not self.running:
                    return
                
                # 更新前一个组的发送计数
                if current_group_name in self.group_send_counts:
                    self.group_send_counts[current_group_name] += 1
                else:
                    self.group_send_counts[current_group_name] = 1
                
                # 添加调试信息，显示前一个组是第几次发送
                self.log_signal.emit(f"第{self.group_send_counts[current_group_name]}次发送，发送的组为：{current_group_name}")
            
            # 如果是新组且处于非循环模式，同样发送进度信号（表示前一个组发送完成）
            if current_group_name is not None and is_new_group and cyclic_mode is False:
                # 添加调试信息，显示前一个组发送完成
                self.log_signal.emit(f"完成发送数据组：{current_group_name}")

            # 如果组名发生变化，需要添加组间延迟
            if current_group_name is not None and current_group_name != group_name:
                op_time = op_timer.elapsed() / 1000.0
                actual_delay = max(0, self.delay - op_time)
                # 在延迟前检查是否需要停止
                if not self.running:
                    return
                self.delay_fuction(actual_delay)

                # 重置计时器用于下一个数据项的发送
                op_timer.restart()
            
            current_group_name = group_name
            
            # 创建临时QListWidgetItem来发送实际数据
            temp_item = QListWidgetItem()
            temp_item.setData(Qt.UserRole, actual_data)
            # 在发送数据前检查是否需要停止
            if not self.running:
                return
            self.send_item_data(temp_item)

            # 数据项之间使用固定0.01秒(10ms)延迟
            if i < (len(items) - 1):
                op_time = op_timer.elapsed() / 1000.0
                # 每个项之间有0.01秒延迟
                actual_delay = max(0, 0.01 - op_time)
                # 在延迟前检查是否需要停止
                if not self.running:
                    return
                self.delay_fuction(actual_delay)
        
        # 循环结束后，处理最后一个组的进度信息
        if current_group_name is not None and cyclic_mode is True:
            if self.spi_controller.driver.dev_handle is None:
                self.running = False
                return
            # 在发出进度信号前检查是否需要停止
            if not self.running:
                return
            
            # 更新最后一个组的发送计数
            if current_group_name in self.group_send_counts:
                self.group_send_counts[current_group_name] += 1
            else:
                self.group_send_counts[current_group_name] = 1
            
            # 添加调试信息，显示最后一个组是第几次发送
            self.log_signal.emit(f"第{self.group_send_counts[current_group_name]}次发送，发送的组为：{current_group_name}")
        
        # 非循环模式下，也要在最后处理最后一个组的信息
        if current_group_name is not None and cyclic_mode is False:
            # 添加调试信息，显示最后一个组发送完成
            self.log_signal.emit(f"完成发送数据组：{current_group_name}")

    # ==================== 线程执行功能 ====================
    def run(self):
        """
        线程执行入口
        
        根据设定的模式执行相应的发送操作。
        """
        self.running = True

        self.group_send_counts = {}

        if self.mode == "circ":
            self.send_cyclic()

        self.running = False
        self.finished_signal.emit()

    # ==================== 线程控制功能 ====================
    def stop(self):
        """
        停止发送任务
        """
        self.running = False

    # ==================== 数据发送功能 ====================
    def send_item_data(self, item):
        """
        发送单个数据项
        
        处理数据项的发送过程，包括CRC校验、设备检查和实际发送。
        
        Args:
            item: 要发送的数据项
        """

        if self.spi_controller.driver.dev_handle is None:
            self.running = False
            return

        if self.running is False:
            return
        
        data_tuple = item.data(Qt.UserRole)

        data_name, data = data_tuple

        # 修改：在发送时动态获取clk_mode和bit_order的当前值
        clk_mode = self.ui.combo_box_clk.currentIndex()
        bit_order = self.ui.combo_box_bit.currentIndex()

        # print(clk_mode, bit_order)

        self.spi_controller.spi_send(data,clk_mode,bit_order, data_name = data_name)
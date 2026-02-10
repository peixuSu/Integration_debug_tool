#!/usr/bin/env python3.13
"""
filename: sub_add_data.py
author: [spx]
email: [3123002434@mail2.gdut.edu.cn]
date: 2025-12-21
description: SPI数据添加子窗口，处理SPI数据的输入和配置
"""

import re
from PySide6.QtWidgets import QMessageBox, QTabWidget, QVBoxLayout
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu, QStatusBar
from PySide6.QtCore import Signal, QTimer
from core.ui.Ui_sub_add_data import Ui_SubForm_Data
from PySide6.QtGui import QAction
from core.sub_window.formula_parser import FormulaParser

class SubWindowAddData(QWidget):
    """
    SPI数据子窗口类，负责处理SPI数据输入和配置相关的UI连接和业务逻辑
    """
    # 定义信号，用于向主窗口发送数据
    data_added = Signal(str, str)

    def __init__(self, application):
        """
        初始化SPI数据子窗口
        
        Args:
            application: 应用实例
        """
        super().__init__()
        # 初始化UI界面
        self.ui = Ui_SubForm_Data()
        self.ui.setupUi(self)
        self.application = application

        self.yaml_window = application.yaml_window

        self.yaml_path = None
        
        # 设置窗口标题
        self.setWindowTitle('SPI 数据窗口')
        
        # 设置文本输入框的占位符提示
        self.ui.line_text.setPlaceholderText("e.g., 00 00 00")
        
        # 当前指令类型标识
        self.now_command = None

        # 设置编辑框同步变化
        self.setup_edit_sync()
        
        # 创建菜单栏
        # 移除了create_tab_widget()调用，因为已在QtDesigner中设计
        
        # 存储指令数据的列表
        self.command = []

        # 创建状态栏并添加到第二页底部
        self.create_status_bar()

        self.connect_yaml_signals()
        
        # 使用QTimer定期检查YAML文件是否已导入
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_yaml_import_status)
        self.timer.start(1000)  # 每1000毫秒（1秒）触发一次

        self.setup_connections()

        # 初始化全局设置
        self.load_global_settings()

    # ==================== 信号连接功能 ====================

    def setup_connections(self):
        """
        设置UI组件的信号与槽函数连接
        """
        # 连接按钮信号与槽函数
        self.ui.button_data_confirm.clicked.connect(self.send_to_main)
        self.ui.button_data_cancel.clicked.connect(self.close)
        self.ui.pushButton_add_data.clicked.connect(self.cal_formula_command)
        
        self.ui.lineEdit_input.textChanged.connect(self.update_preview)
        
        self.ui.comboBox_function.currentIndexChanged.connect(self.update_preview)

    def load_global_settings(self):
        """
        从YAML文件加载全局设置并更新UI控件
        """
        if self.yaml_window.file_path:
            settings = self.yaml_window.get_global_settings()
            if settings:
                # 更新UI控件显示
                self.ui.lineEdit_lane.setText(settings.get('channel', ''))
                self.ui.lineEdit_color_depth.setText(settings.get('color_depth', ''))
                self.ui.lineEdit_width.setText(settings.get('horizontal_resolution', ''))
                self.ui.lineEdit_height.setText(settings.get('vertical_resolution', ''))
                
                # 更新实时预览
                self.update_preview

    # ==================== 实时预览功能 ====================

    def update_preview(self):
        """
        实时更新预览命令和函数名称显示
        """
        # 获取当前选中的功能
        current_index = self.ui.comboBox_function.currentIndex()
        if current_index < 0:
            self.ui.label_sample.setText("请选择功能")
            self.ui.label_name_show.clear()
            return

        # 获取选中项关联的数据
        data = self.ui.comboBox_function.itemData(current_index)
        if not data:
            self.ui.label_sample.setText("未找到对应的功能配置")
            self.ui.label_name_show.clear()
            return

        function, formula, var_name, input_radix, address, data_width = data

        # 更新函数名称显示（整合原来update_function_name_display的功能）
        if function:
            # 获取输入框中的数字
            input_number = self.ui.lineEdit_input.text().strip()
            function_with_suffix = f"{function}{input_number}"
            self.ui.label_name_show.setText(function_with_suffix)
        else:
            self.ui.label_name_show.clear()

        # print(f"当前选择的功能: {function}, 公式: {formula}, 变量名: {var_name}, 范围: {input_range}, 地址: {address}, 符号位宽度: {data_width}")

        # 获取当前输入值
        input_value_text = self.ui.lineEdit_input.text()
        if not input_value_text:
            self.ui.label_sample.setText("请输入值")
            return

        try:
            # 获取function_config_window_instance以获取范围和符号位设置
            function_config_data = self.application.sub_window.function_config_window_instance.get_configs()
            selected_config = None
            for config in function_config_data:
                if config.get('function') == function or config.get('address') == address:
                    selected_config = config
                    break

            if not selected_config:
                self.ui.label_sample.setText(f"未找到功能 {function} 的配置信息")
                return

            # 将输入值转换为十进制数，支持十进制和十六进制
            input_value = self.hex_to_dec(input_value_text,input_radix)

            # 直接使用data_width字段来判断数据位宽
            parser = FormulaParser()
            formula_variables = parser.extract_variables(formula)

            # 根据公式中的变量构建变量字典
            var_dict = {}

            if var_name and len(var_name) > 0:
                # 如果var_name中定义了变量，将输入值分配给第一个变量
                var_dict[var_name] = input_value

            # 检查公式中是否包含多变量（通道、色深、分辨率等）
            for formula_var in formula_variables:
                if formula_var not in var_dict:  # 只处理不在var_dict中的变量
                    # 从YAML的global_settings获取值
                    if formula_var == "通道":
                        var_dict[formula_var] = int(self.ui.lineEdit_lane.text())
                    elif formula_var == "色深":
                        var_dict[formula_var] = int(self.ui.lineEdit_color_depth.text())
                    elif formula_var == "水平分辨率":
                        var_dict[formula_var] = int(self.ui.lineEdit_width.text())
                    elif formula_var == "垂直分辨率":
                        var_dict[formula_var] = int(self.ui.lineEdit_height.text())

            # 计算公式结果
            result = FormulaParser.calculate_formula_result(formula, var_dict)

            # 根据data_width设置处理结果
            # 如果data_width是"低8bit"，则取结果的低8bit，高8位为0
            # 如果data_width是"全部16bit"，则保留全部16bit结果
            if '低8bit' in data_width:
                result = int(result) & 0x00FF  # 取低8bit，高8位为0
                hex_result = f"{result:04X}"  # 4位十六进制
            else:  # 默认保留全部16bit
                result = int(result) & 0xFFFF  # 限制在16bit范围内
                hex_result = f"{result:04X}"  # 4位十六进制

            # print(f"计算结果为: {hex_result}")
            # print(f"data_width: {data_width}")

            # 获取帧头 - 从YAML的global_settings获取，如果不存在则使用默认值
            global_settings = self.yaml_window.get_global_settings()
            head = global_settings.get('frame_head', '40')
            
            # 将四位16进制数分成两位两位的形式
            hex_part1 = hex_result[:2]  # 前两位
            hex_part2 = hex_result[2:]  # 后两位
            
            preview_command = f"{head} {address} {hex_part1} {hex_part2}"
            self.ui.label_sample.setText(f"预览: {preview_command}")

        except ValueError as e:
            # 输入值不是有效数字
            self.ui.label_sample.setText("输入值格式错误")
        except Exception as e:
            # 其他错误
            self.ui.label_sample.setText(f"计算错误: {str(e)}")

    def hex_to_dec(self, input_text, input_radix=None):
        """
        将输入的文本转换为十进制数，支持十进制和十六进制输入
        根据input_radix参数决定输入格式
        
        Args:
            input_text (str): 输入的文本
            input_radix (str): 输入进制类型，如"十进制"或"十六进制"
            
        Returns:
            float: 转换后的十进制数
        """
        input_text = input_text.strip()
        
        # 检查是否为十六进制格式（带 0x 或 0X 前缀），这种情况总是按十六进制处理
        if input_text.lower().startswith('0x'):
            # 是十六进制数，去掉前缀并转换
            hex_part = input_text[2:]  # 去掉 '0x' 前缀
            try:
                return float(int(hex_part, 16))
            except ValueError:
                raise ValueError(f"无效的十六进制数: {hex_part}")
        else:
            # 根据input_radix参数决定处理方式
            if input_radix and ("十六进制" in input_radix or "hex" in input_radix.lower()):
                # 按十六进制处理
                try:
                    return float(int(input_text, 16))
                except ValueError:
                    raise ValueError(f"无效的十六进制数: {input_text}")
            else:
                # 按十进制处理（默认）
                try:
                    return float(input_text)
                except ValueError:
                    raise ValueError(f"无效的十进制数: {input_text}")

    # ==================== YAML文件处理功能 ====================

    def check_yaml_import_status(self):
        """
        定期检查YAML文件导入状态并更新界面
        """
        # 检查是否有导入的YAML文件路径
        if self.yaml_window.file_path:
            # 如果已经有导入的文件路径但状态栏未更新，则更新状态栏
            if self.yaml_path != self.yaml_window.file_path:
                self.yaml_path = self.yaml_window.file_path
                self.status_bar.showMessage(f"已导入yaml文件: {self.yaml_path}", 0)
                
                # 更新comboBox_function
                self.update_combo_box_function(self.yaml_path)
                
                # 加载全局设置
                self.load_global_settings()
        else:
            # 如果没有导入的文件，保持就绪状态
            if self.status_bar.currentMessage() == "":
                self.status_bar.showMessage("未导入文件", 0)

    def connect_yaml_signals(self):
            """
            连接YAML窗口的信号到状态栏更新函数
            """
            # 连接导入信号到状态栏更新函数
            self.yaml_window.import_signal.connect(self.update_status_bar_on_import)
            # 连接导入信号到comboBox_function更新函数
            self.yaml_window.import_signal.connect(self.update_combo_box_function)
            # 连接导入信号到全局设置更新函数
            self.yaml_window.import_signal.connect(lambda file_path: self.load_global_settings())
            # print("连接YAML信号")

    def update_combo_box_function(self, file_path):
        """
        当YAML文件导入时更新comboBox_function
        
        Args:
            file_path: 导入的文件路径
        """
        # 从function_config_window_instance获取配置数据
        function_config_data = self.application.sub_window.function_config_window_instance.get_configs()
        
        # 检查数据是否为空
        if not function_config_data:
            return
        
        # 使用blockSignals临时阻止信号发射
        self.ui.comboBox_function.blockSignals(True)
        
        # 清空comboBox_function的现有项
        self.ui.comboBox_function.clear()

        # 从function_config中提取功能并添加到comboBox_function
        for i, item in enumerate(function_config_data):
            address = item.get('address')
            function = item.get('function', '')
            var_name = item.get('var_name', '')
            formula = item.get('formula', '')
            input_radix = item.get('input_radix', '')
            data_width = item.get('data_width', '') 

            var_name = self.clean_var_name(var_name)
            
            if function:  # 使用功能名称作为显示项
                # 存储一个元组作为itemData，包含所有相关信息
                data_tuple = (function, formula, var_name, input_radix, address, data_width)
                self.ui.comboBox_function.addItem(function, data_tuple)
        
        # 恢复信号发射
        self.ui.comboBox_function.blockSignals(False)

        # 重新连接信号
        self.ui.comboBox_function.currentIndexChanged.connect(self.display_function)
        
        # 主动触发一次索引改变来显示最后一个功能对应的信息
        if self.ui.comboBox_function.count() > 0:  # 有功能项
            self.ui.comboBox_function.setCurrentIndex(self.ui.comboBox_function.count() - 1)  # 选择最后一个功能项
            # 手动触发一次显示更新，确保label_sample被正确更新
            self.display_function(self.ui.comboBox_function.currentIndex())

    def display_function(self, index):
        """
        根据comboBox_function的选择显示对应的功能和公式
        
        Args:
            index: comboBox_function的当前索引
        """
        # 检查索引是否有效
        if index < 0:
            # 索引无效，清空显示
            self.ui.label_name_show.clear()
            self.ui.textEdit_formula.clear()
            self.ui.label_sample.clear()
            self.ui.lineEdit_input.clear()
            return
            
        # 获取选中项关联的功能数据
        data = self.ui.comboBox_function.itemData(index)
        
        function, formula, var_name, input_radix , address, data_width = data

        # 显示公式数据
        if formula:
            self.ui.textEdit_formula.setText(formula)
        else:
            self.ui.textEdit_formula.clear()

        # 设置输入框的占位符提示
        if input_radix :
            self.ui.lineEdit_input.setPlaceholderText(f"请输入{input_radix}")

        # 更新实时预览
        self.update_preview

    def update_status_bar_on_import(self, file_path):
        """
        当YAML文件导入时更新状态栏
        
        Args:
            file_path: 导入的文件路径
        """
        # 更新状态栏显示导入成功的消息
        self.status_bar.showMessage(f"已导入项目: {file_path}", 0)
        self.yaml_path = file_path

    # ==================== 界面组件功能 ====================

    def create_status_bar(self):
        """
        创建状态栏并添加到第二页底部
        """
        # 创建状态栏
        self.status_bar = QStatusBar(self)
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #f0f0f0;
                border-top: 1px solid #d0d0d0;
                font-size: 9px;
                padding: 1px;
                min-height: 18px;
                max-height: 18px;
            }
        """)
        
        # 将状态栏添加到tab_2的布局中
        tab_2_layout = self.ui.tab_2.layout()

        tab_2_layout.addWidget(self.status_bar)

        
        # 设置初始状态消息
        self.status_bar.showMessage("无yaml导入", 0)  # 0表示永久显示

    def clean_var_name(self, var_name):
        """
        清理var_name字段，移除其中包含的额外参数
        
        Args:
            var_name (str): 原始变量名称
            
        Returns:
            str: 清理后的变量名称
        """

        # 定义需要移除的额外参数列表
        extra_params = ["通道", "色深", "水平分辨率", "垂直分辨率"]
        
        # 移除这些额外参数
        cleaned_var_name = var_name
        for param in extra_params:
            cleaned_var_name = cleaned_var_name.replace(param, "")
        
        # 移除多余的逗号和空格
        # 处理类似 "对比度,,通道" 的情况
        cleaned_var_name = re.sub(r',+', ',', cleaned_var_name)  # 将多个连续逗号替换为单个逗号
        cleaned_var_name = re.sub(r'^,+|,+$', '', cleaned_var_name)  # 移除开头和结尾的逗号
        cleaned_var_name = cleaned_var_name.strip()  # 移除首尾空格
        
        return cleaned_var_name

    # ==================== 数据处理功能 ====================

    def setup_edit_sync(self):
        """
        设置 编辑框 同步变化
        
        此处可以设置其他需要同步变化的编辑框
        注意：lineEdit_width 和 lineEdit_height 不再同步变化，因为它们代表不同分辨率
        """
        # 标志位，用于防止编辑框变化时的递归调用
        self._updating = False
        
        # 当前不需要任何编辑框同步变化
        # width和height分别代表水平分辨率和垂直分辨率，应该独立变化

    # ==================== 指令计算功能 ====================

    def cal_formula_command(self):
        """
        通过formula计算指令
        
        根据当前选中的功能和输入的值，使用formula计算数据
        """
        
        # 检查是否已导入YAML文件
        if not self.yaml_window.file_path:
            QMessageBox.warning(self, 'warning', '请先导入YAML项目文件.')
            return

        # 获取帧头 - 从YAML的global_settings获取，如果不存在则使用默认值
        global_settings = self.yaml_window.get_global_settings()
        head = global_settings.get('frame_head', '40')

        # 获取当前选中的功能
        current_index = self.ui.comboBox_function.currentIndex()
        function_name = self.ui.comboBox_function.currentText()    

        # 获取选中项关联的数据
        data = self.ui.comboBox_function.itemData(current_index)
        if not data:
            QMessageBox.warning(self, 'warning', '未找到对应的功能配置.')
            return

        function, formula, var_name, input_radix, address, data_width = data

        # 获取输入值
        input_value_text = self.ui.lineEdit_input.text()
        if not input_value_text:
            QMessageBox.warning(self, 'warning', '请输入有效数值.')
            return

        # 获取function_config_window_instance以获取范围和符号位设置
        try:
            function_config_data = self.application.sub_window.function_config_window_instance.get_configs()
            selected_config = None
            for config in function_config_data:
                if config.get('function') == function_name or config.get('address') == address:
                    selected_config = config
                    break

            if not selected_config:
                QMessageBox.warning(self, 'warning', f'未找到功能 {function_name} 的配置信息.')
                return

            # 将输入值转换为十进制数，支持十进制和十六进制
            input_value = self.hex_to_dec(input_value_text,input_radix)

            # 直接使用data_width字段来判断数据位宽
            parser = FormulaParser()
            formula_variables = parser.extract_variables(formula)

            # 根据公式中的变量构建变量字典
            var_dict = {}

            if var_name and len(var_name) > 0:
                # 如果var_name中定义了变量，将输入值分配给第一个变量
                var_dict[var_name] = input_value

            # 检查公式中是否包含多变量（通道、色深、分辨率等）
            for formula_var in formula_variables:
                if formula_var not in var_dict:  # 只处理不在var_dict中的变量
                    # 从YAML的global_settings获取值，如果不存在则从UI控件获取
                    if formula_var == "通道":
                        var_dict[formula_var] = int(self.ui.lineEdit_lane.text())
                    elif formula_var == "色深":
                        var_dict[formula_var] = int(self.ui.lineEdit_color_depth.text())
                    elif formula_var == "水平分辨率":
                        var_dict[formula_var] = int(self.ui.lineEdit_width.text())
                    elif formula_var == "垂直分辨率":
                        var_dict[formula_var] = int(self.ui.lineEdit_height.text())

            # 计算公式结果
            result = FormulaParser.calculate_formula_result(formula, var_dict)

            if '低8bit' in data_width:
                result = int(result) & 0x00FF  # 取低8bit，高8位为0
                hex_result = f"{result:04X}"  # 4位十六进制
            else:  # 默认保留全部16bit
                result = int(result) & 0xFFFF  # 限制在16bit范围内
                hex_result = f"{result:04X}"  # 4位十六进制

            # 构建最终命令
            command_name = f"{function}{input_value_text}"

            final_command = f"{head} {address} {hex_result}"

            # 发送数据到主窗口
            self.data_added.emit(command_name, final_command)

            # 清空输入框
            self.ui.lineEdit_input.clear()

        except ValueError as e:
            # 输入值不是有效数字
            QMessageBox.warning(self, 'warning', f'输入值格式错误: {str(e)}')
        except Exception as e:
            # 其他错误
            QMessageBox.warning(self, 'warning', f'计算错误: {str(e)}')

    def send_to_main(self):
        """
        发送数据到主窗口
        """
        # 获取输入的数据
        data_name = self.ui.line_name.text()
        data_content = self.ui.line_text.text()

        if not data_name or not data_content:
            # 显示警告消息
            QMessageBox.warning(self, 'warning', '请填写完整数据信息.')
            return

        # 发送数据到主窗口
        self.data_added.emit(data_name, data_content)

        # 关闭窗口
        self.close()

    def get_data(self):
        """
        获取输入的数据
        
        Returns:
            tuple: 包含数据名称和数据内容的元组
        """
        # 返回输入的数据
        return self.ui.line_name.text(), self.ui.line_text.text()
#!/usr/bin/env python3.13
"""
filename: yaml_window.py
author: [spx]
email: [3123002434@mail2.gdut.edu.cn]
date: 2025-12-21
description: YAML连接主窗口，处理YAML相关的UI连接和业务逻辑
"""

import yaml
import os
from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtWidgets import QFileDialog, QMessageBox
from .yaml_template import YAMLTemplate



class YAMLWindow(QObject):
    """
    YAML连接主窗口类，处理YAML相关的UI连接和业务逻辑
    """

    import_signal = Signal(str)

    def __init__(self, application):
        """
        初始化YAML连接主窗口
        
        Args:
            application: 应用程序实例
        """
        super().__init__()
        self.application = application
        self.ui = application.ui
        self.file_path = None
        self.setup_connections()
        # self.yaml_loadeding = False

    def setup_connections(self):
        """
        设置YAML相关控件的连接信号槽
        """
        self.ui.button_new_prj.clicked.connect(self.create_new_prj)
        self.ui.button_import_prj.clicked.connect(self.import_prj)
        self.ui.line_prj_name.editingFinished.connect(self.update_project_name)

    def create_new_prj(self):
        """
        创建新的YAML项目
        """
        
        # # 弹出确认对话框，询问用户是否创建新项目
        # reply = QMessageBox.information(
        #     self.application,
        #     "提示",
        #     "创建新项目将清空当前数据，是否继续？",
        #     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        # )

        # # 如果用户选择否，则返回不执行任何操作
        # if reply == QMessageBox.StandardButton.No:
        #     return
        
        # # 清空所有现有数据
        # self.clear_all()

        # 获取默认的YAML模板数据
        default_data = YAMLTemplate.create_template()

        # 打开文件保存对话框，让用户选择保存位置
        file_path, _ = QFileDialog.getSaveFileName(
            self.application,
            "保存新项目",
            "新建项目.yml",
            "YAML Files (*.yml *.yaml)"
        )

        if not file_path:
            return

        # 如果用户选择了保存路径，则保存文件
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                yaml.dump(
                    default_data, 
                    file, 
                    allow_unicode=True, 
                    default_flow_style=False,
                    sort_keys=False
                )
        
        # 保存文件路径
        self.file_path = file_path

        # 设置默认的数据组和测试组
        default_data_group = {'默认组': {'data': []}}
        default_test_group = {'新建分组1': []}

        # # 初始化测试组和数据组管理器
        self.application.test_group_window.test_group_manager.set_test_group(default_test_group)
        self.application.data_group_window.data_group_manager.set_data_group(default_data_group)

        self.ui.line_prj_name.setText(default_data['project_name'])

        self.ui.button_function_config.setEnabled(True)

        self.import_signal.emit(self.file_path)

    def import_prj(self):
        """
        导入YAML项目
        """

        # 打开打开文件选择对话框，让用户选择要导入的项目文件，让用户选择要导入的项目文件
        file_path, _ = QFileDialog.getOpenFileName(
            self.application,
            "导入项目",
            "",
            "YAML Files (*.yml *.yaml)"
        )

        # 如果用户没有选择文件，则返回
        if file_path is None or file_path == "":
            return
        
        # 保存文件路径
        self.file_path = file_path

        print(f"当前的文件路径为: {self.file_path}")

        # self.yaml_loadeding = True

        # 读取选定的YAML文件
        with open(file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {}

        # 检查并添加缺失的function_config字段以确保向后兼容
        if 'function_config' not in config:
            config['function_config'] = []
            
            with open(self.file_path, 'w', encoding='utf-8') as file:
                yaml.dump(
                    config, 
                    file, 
                    allow_unicode=True, 
                    default_flow_style=False,
                    sort_keys=False
                )
            # print("导入的项目不包含功能配置")
        # else:
            # print("导入的项目包含功能配置")

        # 如果配置中包含项目名称，则设置到界面中
        if 'project_name' in config:
            self.ui.line_prj_name.setText(config['project_name'])

        # 如果配置中包含SPI配置，则设置到界面中
        if 'spi_config' in config:
            spi_config = config['spi_config']
            if 'vcc' in spi_config:
                index = self.ui.combo_box_vcc.findText(spi_config['vcc'])
                if index >= 0:
                    self.ui.combo_box_vcc.setCurrentIndex(index)
            if 'io' in spi_config:
                index = self.ui.combo_box_io.findText(spi_config['io'])
                if index >= 0:
                    self.ui.combo_box_io.setCurrentIndex(index)
            if 'speed' in spi_config:
                index = self.ui.combo_box_speed.findText(spi_config['speed'])
                if index >= 0:
                    self.ui.combo_box_speed.setCurrentIndex(index)
            if 'clk' in spi_config:
                index = self.ui.combo_box_clk.findText(spi_config['clk'])
                if index >= 0:
                    self.ui.combo_box_clk.setCurrentIndex(index)
            if 'bit' in spi_config:
                index = self.ui.combo_box_bit.findText(spi_config['bit'])
                if index >= 0:
                    self.ui.combo_box_bit.setCurrentIndex(index)
            if 'rx_size' in spi_config:
                index = self.ui.combo_box_size.findText(spi_config['rx_size'])
                if index >= 0:
                    self.ui.combo_box_size.setCurrentIndex(index)

        # 转换数据格式以适应 set_data_group 方法
        data_group = {}
        for group_name, group_content in config['data_group'].items():
            # 将字典格式转换为元组列表
            converted_data = []
            if 'data' in group_content:
                for item in group_content['data']:
                    # 将字典转换为元组
                    converted_data.append((item['name'], item['data']))

            data_group[group_name] = {'data': converted_data}
        
        # 使用 set_data_group 方法设置数据
        self.application.data_group_window.data_group_manager.set_data_group(data_group)


        # 转换数据格式以适应 set_test_group 方法
        test_group = {}
        for group_name, items in config['test_group'].items():
            # 将字典格式转换为元组列表
            converted_items = []
            for item in items:
                # 将字典转换为元组
                converted_items.append((item['name'], item['data']))
            
            test_group[group_name] = converted_items
        
        # 使用 set_test_group 方法设置数据
        self.application.test_group_window.test_group_manager.set_test_group(test_group)
        
        self.application.test_group_window.select_all_changed(Qt.Checked)

        self.application.ui.check_box_select_all.setChecked(True)

        # 设置到功能配置窗口中
        if 'function_config' in config:
            function_config = config['function_config']
            
            # 检查是否需要更新旧版本YAML格式
            needs_update = any('range_val' in item or 'sign' in item or 'multi_var' in item or 'sign_width' in item or 'input_range' in item for item in function_config)
            
            # 在处理旧版本字段映射时，对于input_range: 无的情况，应该映射为十进制
            input_radix_value = item.get('input_radix', item.get('input_range', item.get('range_val', '十进制')))
            # 处理旧版本的 '无' 值，将其转换为 '十进制'
            if input_radix_value == '无':
                input_radix_value = '十进制'

            # 为了兼容旧版本YAML格式，转换功能配置数据
            converted_function_config = []
            for item in function_config:
                # 处理旧版本字段映射到新版本
                
                converted_item = {
                    'address': item.get('address', ''),
                    'record': item.get('record', ''),
                    'function': item.get('function', ''),
                    'var_name': item.get('var_name', ''),
                    'formula': item.get('formula', ''),
                    'input_radix': input_radix_value,
                    'data_width': item.get('data_width', item.get('sign_width', '低8bit'))  # 兼容旧字段名sign_width
                }
                
                # 如果input_range或sign_width存在但新字段不存在，给出默认值
                if 'input_range' in item and 'input_radix' not in converted_item:
                    # 旧版的input_range通常表示范围限制，现在改为进制选择
                    converted_item['input_radix'] = '十进制'
                    
                if 'sign_width' in item and 'data_width' not in converted_item:
                    # 从旧的sign_width映射到新的data_width
                    old_sign_width = item.get('sign_width', '')
                    if old_sign_width in ['低8bit', 'low8bit', 'Low8Bit']:
                        converted_item['data_width'] = '低8bit'
                    elif old_sign_width in ['全16bit', 'all16bit', 'All16Bit']:
                        converted_item['data_width'] = '全16bit'
                    else:
                        converted_item['data_width'] = '低8bit'  # 默认值
                
                # 如果是旧版本格式，其他旧字段也不再需要，只保留新字段
                converted_function_config.append(converted_item)
            
            # 如果检测到旧格式，更新YAML文件
            if needs_update:
                config['function_config'] = converted_function_config
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    yaml.dump(
                        config, 
                        file, 
                        allow_unicode=True, 
                        default_flow_style=False,
                        sort_keys=False
                    )
            
            # 将转换后的功能配置数据传递给功能配置窗口
            self.application.sub_window.function_config_window_instance.load_function_config(converted_function_config)

        # 检查并添加缺失的global_settings字段以确保向后兼容
        if 'global_settings' not in config:
            # 定义默认的全局设置，参考模板文件中的结构
            default_global_settings = {
                'frame_head': '40',
                'channel': '8',
                'color_depth': '1024',
                'horizontal_resolution': '3840',
                'vertical_resolution': '2160'
            }
            config['global_settings'] = default_global_settings
            
            # 将更新后的配置写回YAML文件
            with open(self.file_path, 'w', encoding='utf-8') as file:
                yaml.dump(
                    config, 
                    file, 
                    allow_unicode=True, 
                    default_flow_style=False,
                    sort_keys=False
                )
        
        # 加载全局设置（帧头、通道、色深、分辨率等）
        global_settings = config['global_settings']
        self.application.sub_window.function_config_window_instance.set_global_settings(global_settings)

        # 启用功能配置按钮
        self.ui.button_function_config.setEnabled(True)

        self.import_signal.emit(self.file_path)

    def update_project_name(self):
        """
        更新项目名称
        """

        project_name = self.ui.line_prj_name.text()

        if not project_name:
            QMessageBox.warning(self.application, "警告", "项目名称不能为空")
            return
        
        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}
        
        # 更新project_name字段
        yaml_data['project_name'] = self.ui.line_prj_name.text()
        
        # 写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

        self.update_spi_config()

    def update_spi_config(self):
        """
        更新SPI配置到YAML文件
        """
        # 检查是否有有效的文件路径
        if self.file_path is None:
            return

        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}

        vcc_text = self.ui.combo_box_vcc.currentText()
        if vcc_text is None or vcc_text == "":
            return

        # print(f"当前的vcc: {self.ui.combo_box_vcc.currentText()}")

        # 更新SPI配置
        yaml_data['spi_config'] = {
            'vcc': self.ui.combo_box_vcc.currentText(),
            'io': self.ui.combo_box_io.currentText(),
            'speed': self.ui.combo_box_speed.currentText(),
            'clk': self.ui.combo_box_clk.currentText(),
            'bit': self.ui.combo_box_bit.currentText(),
            'rx_size': self.ui.combo_box_size.currentText(),
        }

        # print(f"yaml类中当前spi配置: {yaml_data['spi_config']}")

        # 将更新后的配置写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

    def update_data_group(self):
        """
        更新数据组
        """

        data_group = self.application.data_group_window.data_group_manager.get_data_group_manager()

        # print(f"yaml类中当前数据组管理器内容: {data_group}")

        if self.file_path is None:
            return

        if not data_group:
            return
        
         # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}
        
        # 准备要保存的数据组数据
        # 需要将元组转换为列表以便正确保存到YAML
        converted_data_group = {}
        for group_name, group_content in data_group.items():
            converted_data = []
            if 'data' in group_content:
                for item in group_content['data']:
                    if isinstance(item, tuple):
                        # 将元组转换为字典格式
                        converted_data.append({
                            'name': item[0],
                            'data': item[1]
                        })
            
            converted_data_group[group_name] = {
                'data': converted_data
            }
        
        # 更新data_group字段
        yaml_data['data_group'] = converted_data_group
        
        # 写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

        self.update_spi_config()
            
        # print(f"数据组已保存到 {self.file_path}")

    def update_test_group(self):
        """
        更新测试组
        """

        # 检查是否有有效的文件路径
        if self.file_path is None:
            return

        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}

        # print("测试程序运行到此处")

        # 获取测试组管理器中的所有测试组数据
        test_group_data = self.application.test_group_window.test_group_manager.get_test_group_manager()

        # print(f"yaml类中当前测试组管理器内容: {test_group_data}")

        # 构造测试组配置
        test_group = {}
        for group_name, items in test_group_data.items():
            test_group[group_name] = []
            for item in items:
                if isinstance(item, tuple) and len(item) >= 2:
                    # 将元组转换为包含 name 和 data 字段的字典
                    test_group[group_name].append({
                        'name': item[0],
                        'data': item[1]
                    })

        # 更新YAML数据中的测试组部分
        yaml_data['test_group'] = test_group

        # print(f"yaml类中当前测试组内容: {test_group}")

        # 将更新后的配置写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

        self.update_spi_config()

    def update_function_config(self):
        """
        更新功能配置到YAML文件
        """
        # 检查是否有有效的文件路径
        if self.file_path is None:
            return
        
        # 获取功能配置数据
        function_config_data = self.application.sub_window.function_config_window_instance.get_configs()

        # print(f"yaml类中当前功能配置内容: {function_config_data}")

        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}

        # 准备要保存的功能配置数据
        converted_function_config = []
        for item in function_config_data:
            # 根据当前系统的字段结构，构造新格式的数据
            converted_item = {
                'address': item.get('address', ''),
                'record': item.get('record', ''),
                'function': item.get('function', ''),
                'var_name': item.get('var_name', ''),
                'formula': item.get('formula', ''),
                'input_radix': item.get('input_radix', '十进制'),  # 新字段：输入进制
                'data_width': item.get('data_width', '低8bit')     # 新字段：数据位宽
            }
            
            converted_function_config.append(converted_item)

        # 更新function_config字段
        yaml_data['function_config'] = converted_function_config

        # 获取全局设置（帧头、通道、色深、分辨率等）
        global_settings = self.application.sub_window.function_config_window_instance.get_global_settings()
        yaml_data['global_settings'] = global_settings

        # 将更新后的配置写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

        # 检查add_data_window_instance是否存在
        if hasattr(self.application.sub_window, 'add_data_window_instance'):
            # 如果实例已存在，直接更新
            self.application.sub_window.add_data_window_instance.update_combo_box_function(self.file_path)
            
    def update_global_settings(self, settings):
        """
        更新全局设置到YAML文件
        参数:
            settings: 全局设置字典，应包含frame_head, channel, color_depth, 
                     horizontal_resolution, vertical_resolution等键
                     参考模板文件中的global_settings结构
        """
        if self.file_path is None:
            return

        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}

        # 更新全局设置
        yaml_data['global_settings'] = settings

        # 将更新后的配置写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )
    
    def get_global_settings(self):
        """
        获取全局设置，如果文件不存在或global_settings字段不存在，则返回默认值
        """
        if self.file_path is None or not os.path.exists(self.file_path):
            # 文件不存在时返回默认值
            return {
                'frame_head': '40',
                'channel': '8',
                'color_depth': '1024',
                'horizontal_resolution': '3840',
                'vertical_resolution': '2160'
            }

        # 读取现有YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}
        
        # 检查是否存在global_settings字段
        if 'global_settings' in yaml_data:
            return yaml_data['global_settings']
        else:
            # 如果不存在则返回默认值，参考模板文件中的结构
            return {
                'frame_head': '40',
                'channel': '8',
                'color_depth': '1024',
                'horizontal_resolution': '3840',
                'vertical_resolution': '2160'
            }

    def update_global_settings(self, settings):
        """
        更新全局设置到YAML文件
        参数:
            settings: 全局设置字典，应包含frame_head, channel, color_depth, 
                     horizontal_resolution, vertical_resolution等键
                     参考模板文件中的global_settings结构
        """
        if self.file_path is None:
            return

        # 读取现有的YAML文件内容
        with open(self.file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file) or {}

        # 更新全局设置
        yaml_data['global_settings'] = settings

        # 将更新后的配置写回YAML文件
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                yaml_data, 
                file, 
                allow_unicode=True, 
                default_flow_style=False,
                sort_keys=False
            )

    def spi_config_set(self):
        """
        手动设置SPI配置
        """
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {}
        
        # 如果配置中包含SPI配置，则设置到界面中
        if 'spi_config' in config:
            spi_config = config['spi_config']
            if 'vcc' in spi_config:
                index = self.ui.combo_box_vcc.findText(spi_config['vcc'])
                if index >= 0:
                    self.ui.combo_box_vcc.setCurrentIndex(index)
            if 'io' in spi_config:
                index = self.ui.combo_box_io.findText(spi_config['io'])
                if index >= 0:
                    self.ui.combo_box_io.setCurrentIndex(index)
            if 'speed' in spi_config:
                index = self.ui.combo_box_speed.findText(spi_config['speed'])
                if index >= 0:
                    self.ui.combo_box_speed.setCurrentIndex(index)
            if 'clk' in spi_config:
                index = self.ui.combo_box_clk.findText(spi_config['clk'])
                if index >= 0:
                    self.ui.combo_box_clk.setCurrentIndex(index)
            if 'bit' in spi_config:
                index = self.ui.combo_box_bit.findText(spi_config['bit'])
                if index >= 0:
                    self.ui.combo_box_bit.setCurrentIndex(index)
            if 'rx_size' in spi_config:
                index = self.ui.combo_box_size.findText(spi_config['rx_size'])
                if index >= 0:
                    self.ui.combo_box_size.setCurrentIndex(index)
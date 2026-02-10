#!/usr/bin/env python3.13
"""
filename: sub_function_config.py
author: [spx]
email: [3123002434@mail2.gdut.edu.cn]
date: 2025-12-23
description: 函数配置子窗口，处理函数相关的配置和设置
"""

import re
from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtWidgets import (
    QMessageBox, QTreeWidgetItem, QStyledItemDelegate, QMenu, QComboBox
)
from PySide6.QtGui import QAction

from core.ui.Ui_sub_function_config import Ui_Form

# 只读代理类
class ReadOnlyDelegate(QStyledItemDelegate):
    """
    只读代理类，用于使特定列不可编辑
    """
    def createEditor(self, parent, option, index):
        """
        重写createEditor方法，返回None表示不创建编辑器
        """
        return None

# 编辑代理类
class EditingDelegate(QStyledItemDelegate):
    """
    编辑代理类，用于处理树形控件的编辑完成信号
    """
    editingFinished = Signal(object, int, str)  # 发送项对象、列号和原始值
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_item = None
        self.current_column = None
        self.original_value = None
        
    def createEditor(self, parent, option, index):
        """
        创建编辑器
        """
        editor = QLineEdit(parent)
        self.current_item = self.parent().itemFromIndex(index)
        self.current_column = index.column()
        
        # 保存原始值
        if self.current_item:
            self.original_value = self.current_item.text(self.current_column)

            editor.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #0078D7;
                selection-background-color: #0078D7;
                selection-color: white;
            }
        """)
        
        # 连接编辑完成信号
        editor.editingFinished.connect(self.on_editing_finished)
        return editor
        
    def on_editing_finished(self):
        """
        处理编辑完成事件
        """
        editor = self.sender()
        if self.current_item and hasattr(self, 'current_column') and hasattr(self, 'original_value'):
            # 强制将编辑器的数据提交到模型
            self.setModelData(editor, self.current_item.treeWidget().model(), 
                             self.current_item.treeWidget().indexFromItem(self.current_item, self.current_column))
            
            # 发出编辑完成信号，包含原始值
            self.editingFinished.emit(self.current_item, self.current_column, self.original_value)
            
    def setModelData(self, editor, model, index):
        """
        将编辑器数据保存到模型
        """
        model.setData(index, editor.text(), Qt.EditRole)

class SubWindowFunctionConfig(QWidget):
    """
    函数配置子窗口类，负责处理函数相关的配置和设置
    """
    # function_config_updated = Signal(dict)

    def __init__(self, application):
        """
        初始化函数配置子窗口类
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.application = application
        self.yaml = application.yaml_window

        # 创建编辑委托实例
        self.editing_delegate = EditingDelegate(self.ui.tree_config)
        self.editing_delegate.editingFinished.connect(self.editing_finished)
        
        # 启用右键菜单
        self.ui.tree_config.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tree_config.customContextMenuRequested.connect(self.show_context_menu)

        self.widget_init()

        self.multi_var = False

    #===============================================================================
    # 初始化UI组件，建立信号槽连接
    #===============================================================================

    def widget_init(self):
        """
        初始化子窗口的UI组件
        """
        self.ui.tree_config.clear()
        self.ui.tree_config.setHeaderLabels([
            "地址", 
            "记录", 
            "功能", 
            "变量名", 
            "公式", 
            "输入进制", 
            "数据位宽"
        ])

        # 添加委托事件
        for i in range(7):
            self.ui.tree_config.setItemDelegateForColumn(i, self.editing_delegate)

        # 添加保存编辑按钮的信号连接
        if hasattr(self.ui, 'pushButton_Save_Edit'):
            self.ui.pushButton_Save_Edit.clicked.connect(self.save_global_settings)

    #===============================================================================
    # 右键菜单功能
    #===============================================================================
    def show_context_menu(self, position):
        """
        显示右键菜单
        """
        # 获取点击的项
        # item = self.ui.tree_config.itemAt(position)
        
        # 创建菜单
        menu = self.create_context_menu()
        # 在鼠标位置显示菜单
        menu.exec(self.ui.tree_config.viewport().mapToGlobal(position))

    def create_context_menu(self):
        """
        创建右键菜单
        """
        menu = QMenu(self)
        add_action = QAction("添加", self)
        add_action.triggered.connect(self.add_new_item)
        menu.addAction(add_action)

        delete_action = QAction("删除", self)
        delete_action.triggered.connect(self.delete_selected_item)
        menu.addAction(delete_action)
        return menu
    
    def add_new_item(self):
        """
        添加新项到tree_config
        """
        # 创建新的树节点
        item = QTreeWidgetItem(self.ui.tree_config)
        item.setText(0, "")  # 地址 - 默认为空

        combo_box_record = QComboBox()
        combo_box_record.addItems(["是", "否"])
        combo_box_record.setCurrentText("是")  # 默认选择"是"
        combo_box_record.currentTextChanged.connect(self.combox_changed)

        self.ui.tree_config.setItemWidget(item, 1, combo_box_record)

        item.setText(2, "")  # 功能 - 默认为空
        item.setText(3, "无")  # 变量名 - 默认为无
        item.setText(4, "无")  # 公式 - 默认为无
        
        combo_box_input_radix = QComboBox()
        combo_box_input_radix.addItems(["十进制", "十六进制"])
        combo_box_input_radix.setCurrentText("十进制")  # 默认选择"十进制"
        combo_box_input_radix.currentTextChanged.connect(self.combox_changed)

        self.ui.tree_config.setItemWidget(item, 5, combo_box_input_radix)

        combo_box_data_width = QComboBox()
        combo_box_data_width.addItems(["低8bit", "全16bit"])
        combo_box_data_width.setCurrentText("低8bit")  # 默认选择"低8bit"
        combo_box_data_width.currentTextChanged.connect(self.combox_changed)
    
        self.ui.tree_config.setItemWidget(item, 6, combo_box_data_width)

        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)  # 允许编辑

        # 设置item的高度和字体
        font = item.font(0)  # 获取第一列的字体
        font.setPointSize(10)  # 设置字体大小
        for i in range(7):  # 应用到所有列
            item.setFont(i, font)

        item.setSizeHint(0, QSize(0, 30))  # 设置高度为30像素

    def delete_selected_item(self):
        """
        删除选中的项
        """
        # 获取当前选中的项
        currentItem = self.ui.tree_config.currentItem()
        if currentItem is None:
            QMessageBox.information(self, "提示", "请先选择要删除的项")
            return

        # 确认删除
        reply = QMessageBox.question(
            self, 
            "确认删除", 
            "确定要删除选中的项吗？", 
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # 获取项的索引并删除
            index = self.ui.tree_config.indexOfTopLevelItem(currentItem)
            if index >= 0:
                self.ui.tree_config.takeTopLevelItem(index)
                # 更新YAML配置
                self.yaml.update_function_config()

    #===============================================================================
    # 编辑完成处理功能
    #===============================================================================

    def editing_finished(self, item, column, original_value):
        """
        处理树项内容改变事件
        """
        # 根据列号调用相应的处理方法
        handlers = {
            0: self.address_edit,
            2: self.function_edit,
            3: self.var_name_edit,
            4: self.formula_edit,
        }
        
        handler = handlers.get(column)
        if handler:
            handler(item, original_value)
        else:
            # 默认处理：更新YAML配置
            self.yaml.update_function_config()

    def address_edit(self, item, original_value):
        """
        处理地址编辑完成事件
        """
        # 获取输入的地址
        addr = item.text(0).strip()

        # 验证输入地址是否存在
        if addr == '':
            QMessageBox.warning(
                self, 
                "警告", 
                "请输入地址！"
            )
            # 恢复原始值
            item.setText(0, original_value)
            return
        
        # 验证输入地址是否有效，并格式化地址
        formatted_addr = self.is_addr_valid(addr)
        if formatted_addr is False:
            QMessageBox.warning(
                self, 
                "警告", 
                "请输入正确的地址格式（00-FF）！"
            )
            # 恢复原始值
            item.setText(0, original_value)
            return

        # 检查是否存在相同的地址（排除当前项）
        old_configs = self.get_configs()

        if old_configs is None:
            # 恢复原始值
            item.setText(0, original_value)
            return

        # 找到当前项的索引
        current_index = -1
        for i in range(self.ui.tree_config.topLevelItemCount()):
            if self.ui.tree_config.topLevelItem(i) == item:
                current_index = i
                break

        # 检查是否存在相同的地址（排除当前项）
        is_same = False
        for i, config in enumerate(old_configs):
            # 排除当前项进行比较
            if i != current_index and config['address'].upper() == formatted_addr.upper():
                is_same = True
                break

        if is_same:
            QMessageBox.warning(
                self, 
                "警告", 
                "该地址已存在！"
            )
            # 恢复原始值
            item.setText(0, original_value)
            return
        
        item.setText(0, formatted_addr)
        self.yaml.update_function_config()

    def function_edit(self, item, original_value):
        """
        处理算法功能编辑完成事件
        """
        # 获取输入的功能
        func = item.text(2).strip()

        # 验证输入功能是否存在
        if func == '':
            QMessageBox.warning(
                self, 
                "警告", 
                "请输入功能！"
            )
            # 恢复原始值
            item.setText(2, original_value)
            return
        
        # 检查是否存在相同的功能（排除当前项）
        old_configs = self.get_configs()

        if old_configs is None:
            # 恢复原始值
            item.setText(2, original_value)
            return

        # 找到当前项的索引
        current_index = -1
        for i in range(self.ui.tree_config.topLevelItemCount()):
            if self.ui.tree_config.topLevelItem(i) == item:
                current_index = i
                break

        # 检查是否存在相同的功能（排除当前项）
        is_same = False
        for i, config in enumerate(old_configs):
            # 排除当前项进行比较
            if i != current_index and config['function'] == func:
                is_same = True
                break

        if is_same:
            QMessageBox.warning(
                self, 
                "警告", 
                "该算法功能已分配给对应的地址！"
            )
            # 恢复原始值
            item.setText(2, original_value)
            return
        
        item.setText(2, func)
        self.yaml.update_function_config()

    def var_name_edit(self, item, original_value):
        """
        处理变量名称编辑完成事件
        """
        # 获取输入的变量名称
        var_name = item.text(3).strip()

        # 处理中文字符
        processed_var_name = self.process_chinese_characters(var_name)
        
        # 如果没有输入变量名称，默认使用"default"
        if processed_var_name == '':
            item.setText(3, "无")
            self.yaml.update_function_config()
            return
        
        # 替换中文逗号为英文逗号并去除多余空格
        processed_var_name = processed_var_name.replace('，', ',').strip()
        
        # 分割变量名称并去除每部分的空格
        var_names = [name.strip() for name in processed_var_name.split(',') if name.strip()]
        
        # 最多允许两个变量
        if len(var_names) > 2:
            QMessageBox.warning(
                self, 
                "警告", 
                "最多只能输入两个变量，用逗号分隔！"
            )
            # 恢复原始值
            item.setText(3, original_value)
            return
        
        # 验证每个变量名称
        for name in var_names:
            var_name_validation = self.check_var_name(name)
            if not var_name_validation["is_valid"]:
                QMessageBox.warning(
                    self, 
                    "警告", 
                    var_name_validation["error_message"]
                )
                # 恢复原始值
                item.setText(3, original_value)
                return
        
        # 将处理后的变量名重新组合（用英文逗号分隔）
        final_var_name = ','.join(var_names)
        
        item.setText(3, final_var_name)
        self.yaml.update_function_config()

    def formula_edit(self, item, original_value):
        """
        处理计算公式编辑完成事件
        """
        var_name = item.text(3).strip()
        
        # 获取输入的公式
        formula = item.text(4).strip()

        # 如果没有输入公式，默认使用"无"
        if formula == '':
            item.setText(4, "无")
            self.yaml.update_function_config()
            return
        
        # 替换中文逗号为英文逗号并去除多余空格
        processed_formula = formula.replace('，', ',').strip()
        
        # 分割公式并去除每部分的空格
        formulas = [f.strip() for f in processed_formula.split(',') if f.strip()]
        
        # 最多允许两个公式
        if len(formulas) > 2:
            QMessageBox.warning(
                self, 
                "警告", 
                "最多只能输入两个公式，用逗号分隔！"
            )
            # 恢复原始值
            item.setText(4, original_value)
            return

        # 检查每个公式的完整性、语法和有效性
        for i, single_formula in enumerate(formulas):
            # 检查公式完整性
            if not self.check_formula_completeness(single_formula):
                QMessageBox.warning(
                    self, 
                    "警告", 
                    f"第{i+1}个公式不完整！"
                )
                # 恢复原始值
                item.setText(4, original_value)
                return

            # 检查语法
            syntax_valid, error_msg = self.check_syntax(single_formula)
            if not syntax_valid:
                QMessageBox.warning(
                    self, 
                    "警告", 
                    f"第{i+1}个公式语法错误：{error_msg}"
                )
                # 恢复原始值
                item.setText(4, original_value)
                return
            
            # 检查公式有效性
            check_formula = self.check_formula(single_formula, var_name)
            if not check_formula["is_valid"]:
                QMessageBox.warning(
                    self, 
                    "警告", 
                    f"第{i+1}个公式出现错误：{check_formula['error_message']}"
                )
                # 恢复原始值
                item.setText(4, original_value)
                return

        # 将处理后的公式重新组合（用英文逗号分隔）
        final_formula = ','.join(formulas)
        
        item.setText(4, final_formula)
        self.yaml.update_function_config()

    def _split_ranges_smart(self, range_string):
        """
        智能分割范围字符串，只在方括号外的逗号处分割
        例如: "[1,2],[3,4]" -> ["[1,2]", "[3,4]"]
            "[1,2]" -> ["[1,2]"]
        """
        ranges = []
        current_part = ""
        bracket_level = 0  # 跟踪方括号的嵌套级别
        
        for char in range_string:
            if char == '[':
                bracket_level += 1
                current_part += char
            elif char == ']':
                bracket_level -= 1
                current_part += char
            elif char == ',' and bracket_level == 0:  # 只有在方括号外的逗号才分割
                # 添加当前部分到结果列表（去除首尾空格）
                part = current_part.strip()
                if part:  # 只添加非空部分
                    ranges.append(part)
                current_part = ""  # 重置当前部分
            else:
                current_part += char
        
        # 添加最后一部分
        part = current_part.strip()
        if part:
            ranges.append(part)
        
        return ranges
    
    #===============================================================================
    # 地址验证功能
    #===============================================================================
    def is_addr_valid(self, addr):
        """
        验证地址格式是否正确
        """
        # 移除可能的0x前缀
        addr = addr.replace("0x", "").replace("0X", "")
        
        # 检查地址长度是否为1-2位十六进制数
        if not re.match(r'^[0-9A-Fa-f]{1,2}$', addr):
            return False
        
        # 返回格式化的地址（大写）
        return addr.upper()

    #===============================================================================
    # 变量名称验证功能
    #===============================================================================
    def check_var_name(self, var_name):
        """
        验证变量名称格式
        """
        if not var_name:
            return {"is_valid": False, "error_message": "变量名不能为空"}
        
        # 检查是否以字母或下划线开头
        if not (var_name[0].isalpha() or var_name[0] == '_'):
            return {"is_valid": False, "error_message": "变量名必须以字母或下划线开头"}
        
        # 检查是否只包含字母、数字和下划线
        if not all(c.isalnum() or c == '_' for c in var_name):
            return {"is_valid": False, "error_message": "变量名只能包含字母、数字和下划线"}
        
        # 检查是否为Python关键字
        import keyword
        if keyword.iskeyword(var_name):
            return {"is_valid": False, "error_message": f"'{var_name}' 是Python关键字，请换一个名称"}
        
        # 检查长度
        if len(var_name) > 50:
            return {"is_valid": False, "error_message": "变量名长度不能超过50个字符"}
        
        return {"is_valid": True}

    #===============================================================================
    # 计算公式验证功能
    #===============================================================================
    def check_formula_completeness(self, formula):
        """
        检查公式是否完整（括号匹配等）
        """
        # 检查括号是否匹配
        stack = []
        for char in formula:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def check_syntax(self, formula):
        """
        检查公式语法
        """
        try:
            # 替换可能的中文运算符
            safe_formula = formula.replace('×', '*').replace('÷', '/')
            
            # 编译公式以检查语法
            compile(safe_formula, '<string>', 'eval')
            return True, ""
        except SyntaxError as e:
            return False, str(e)
        except Exception as e:
            return False, str(e)

    def check_formula(self, formula, var_name):
        """
        检查公式的有效性
        """
        try:
            # 替换可能的中文运算符
            safe_formula = formula.replace('×', '*').replace('÷', '/')
            
            # 特殊处理：如果公式是"无"，则直接返回有效
            if safe_formula == "无":
                return {"is_valid": True}
            
            # 检查是否是多个公式（用逗号分隔）
            formulas = [f.strip() for f in safe_formula.split(',')]
            
            # 检查是否是多个变量（用逗号分隔）
            var_names = []
            if var_name and var_name != "无":
                var_names = [name.strip() for name in var_name.split(',') if name.strip() and name != "无"]
            
            # 创建预设参数字典
            preset_params = {
                "通道": 1,
                "色深": 8,
                "水平分辨率": 1920,
                "垂直分辨率": 1080
            }
            
            # 验证每个公式
            for i, single_formula in enumerate(formulas):
                # 特殊处理：如果单个公式是"无"，跳过验证
                if single_formula == "无":
                    continue
                    
                # 创建局部变量环境
                local_vars = {}
                
                # 添加预设参数
                for key, value in preset_params.items():
                    if key in single_formula:
                        local_vars[key] = value
                
                # 根据公式序号分配对应的变量
                if i < len(var_names):
                    # 为当前公式分配对应的变量
                    local_vars[var_names[i]] = i + 1  # 给变量赋一个测试值
                
                # 尝试计算单个公式
                eval(single_formula, {"__builtins__": {}}, local_vars)
            
            return {"is_valid": True}
        except Exception as e:
            return {"is_valid": False, "error_message": f"公式计算错误: {str(e)}"}
            
    #===============================================================================
    # 中文字符处理功能
    #===============================================================================
    def process_chinese_characters(self, text):
        """
        处理文本中的中文字符，将其转换为英文字符
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 处理后的文本
        """
        if not text:
            return ""
        
        # 中文符号到英文符号的映射
        chinese_to_english = {
            '（': '(',
            '）': ')',
            '＋': '+',
            '－': '-',  # 注意这里是中文的减号
            '×': '*',   # 中文乘号
            '÷': '/',   # 中文除号
            '＝': '=',   # 中文等号
            '《': '<',   # 中文小于号
            '》': '>',   # 中文中号
            '【': '[',   # 中文方括号
            '】': ']',   # 中文方括号
            '｛': '{',   # 中文花括号
            '｝': '}',   # 中文花括号
            '，': ',',   # 中文逗号
            '。': '.',   # 中文句号
            '；': ';',   # 中文分号
            '：': ':',   # 中文冒号
            '“': '"',   # 中文双引号
            '”': '"',   # 中文双引号
            '‘': "'",   # 中文单引号
            '’': "'",   # 中文单引号
        }
        
        # 替换中文符号为英文符号
        processed_text = text
        for chinese, english in chinese_to_english.items():
            processed_text = processed_text.replace(chinese, english)

        return processed_text

    #===============================================================================
    # 数据加载和获取功能
    #===============================================================================
    def load_function_config(self, config_data):
        """
        从YAML加载功能配置数据
        
        Args:
            config_data: 从YAML文件读取的功能配置数据
        """
        # 清空现有配置
        self.ui.tree_config.clear()
        
        # 添加配置项
        for item in config_data:
            addr = item.get('address', '')
            record = item.get('record', '')
            func = item.get('function', '')
            var_name = item.get('var_name', '')
            formula = item.get('formula', '')
            input_radix = item.get('input_radix', '')
            data_width = item.get('data_width', '')
            
            # 创建新的树节点
            tree_item = QTreeWidgetItem(self.ui.tree_config)
            tree_item.setText(0, addr)
            
            combo_box_record = QComboBox()
            combo_box_record.addItems(["是", "否"])
            combo_box_record.setCurrentText(record)

            combo_box_record.currentTextChanged.connect(self.combox_changed)

            self.ui.tree_config.setItemWidget(tree_item, 1, combo_box_record)

            tree_item.setText(2, func)
            tree_item.setText(3, var_name)
            tree_item.setText(4, formula)

            combo_box_input_radix = QComboBox()
            combo_box_input_radix.addItems(["十进制", "十六进制"])
            combo_box_input_radix.setCurrentText(input_radix)
            combo_box_input_radix.currentTextChanged.connect(self.combox_changed)

            self.ui.tree_config.setItemWidget(tree_item, 5, combo_box_input_radix)

            combo_box_data_width = QComboBox()
            combo_box_data_width.addItems(["低8bit", "全16bit"])
            combo_box_data_width.setCurrentText("data_width")
            combo_box_data_width.currentTextChanged.connect(self.combox_changed)

            self.ui.tree_config.setItemWidget(tree_item, 6, combo_box_data_width)

            tree_item.setFlags(tree_item.flags() | Qt.ItemFlag.ItemIsEditable)  # 允许编辑

            # 设置item的高度和字体
            font = tree_item.font(0)  # 获取第一列的字体
            font.setPointSize(10)  # 设置字体大小
            for i in range(8):  # 应用到所有列
                tree_item.setFont(i, font)

            tree_item.setSizeHint(0, QSize(0, 30))  # 设置高度为30像素

    def combox_changed(self):
        """
        处理记录列下拉框变化事件
        """

        # 更新YAML配置文件
        self.yaml.update_function_config()

    def get_configs(self):
        """
        获取当前配置数据
        """
        configs = []
        for i in range(self.ui.tree_config.topLevelItemCount()):
            item = self.ui.tree_config.topLevelItem(i)
            combo_box_record = self.ui.tree_config.itemWidget(item, 1)
            record = combo_box_record.currentText()

            combo_box_input_radix = self.ui.tree_config.itemWidget(item, 5)
            input_radix = combo_box_input_radix.currentText()

            combo_box_data_width = self.ui.tree_config.itemWidget(item, 6)
            data_width = combo_box_data_width.currentText()

            config = {
                'address': item.text(0),
                'record': record,
                'function': item.text(2),
                'var_name': item.text(3),
                'formula': item.text(4),
                'input_radix': input_radix,
                'data_width': data_width  # 数据位宽
            }
            configs.append(config)
        return configs
    
    def get_global_settings(self):
        """
        获取全局设置（帧头、通道、色深、分辨率等）
        """
        global_settings = {
            'frame_head': self.ui.lineEdit_Frame_Head.text(),
            'channel': self.ui.lineEdit_Channal.text(),
            'color_depth': self.ui.lineEdit_Color_Depth.text(),
            'horizontal_resolution': self.ui.lineEdit_Horizontal_Resolution.text(),
            'vertical_resolution': self.ui.lineEdit_Vertical_Resolution.text()
        }
        return global_settings

    def set_global_settings(self, settings):
        """
        设置全局设置（帧头、通道、色深、分辨率等）
        """
        if settings:
            self.ui.lineEdit_Frame_Head.setText(settings.get('frame_head', '40'))
            self.ui.lineEdit_Channal.setText(settings.get('channel', '8'))
            self.ui.lineEdit_Color_Depth.setText(settings.get('color_depth', '1024'))
            self.ui.lineEdit_Horizontal_Resolution.setText(settings.get('horizontal_resolution', '3840'))
            self.ui.lineEdit_Vertical_Resolution.setText(settings.get('vertical_resolution', '2160'))

    def save_global_settings(self):
        """
        保存全局设置到YAML文件
        """
        # 获取当前输入值
        frame_head = self.ui.lineEdit_Frame_Head.text().strip()
        channel = self.ui.lineEdit_Channal.text().strip()
        color_depth = self.ui.lineEdit_Color_Depth.text().strip()
        horizontal_resolution = self.ui.lineEdit_Horizontal_Resolution.text().strip()
        vertical_resolution = self.ui.lineEdit_Vertical_Resolution.text().strip()

        # 验证帧头（16进制数）
        if frame_head:
            try:
                # 验证是否为有效的16进制数
                if frame_head.startswith('0x') or frame_head.startswith('0X'):
                    int(frame_head, 16)
                else:
                    int(frame_head, 16)
            except ValueError:
                QMessageBox.warning(self, "警告", "帧头必须是有效的16进制数！")
                return

        # 验证其余字段（10进制数）
        for value, name in [(channel, "通道"), (color_depth, "色深"), 
                           (horizontal_resolution, "水平分辨率"), (vertical_resolution, "垂直分辨率")]:
            if value:
                try:
                    int(value)
                except ValueError:
                    QMessageBox.warning(self, "警告", f"{name}必须是有效的10进制数！")
                    return

        # 如果所有验证都通过，保存到YAML文件
        global_settings = {
            'frame_head': frame_head or '40',
            'channel': channel or '8',
            'color_depth': color_depth or '1024',
            'horizontal_resolution': horizontal_resolution or '3840',
            'vertical_resolution': vertical_resolution or '2160'
        }

        # 更新YAML文件
        try:
            self.yaml.update_global_settings(global_settings)
            QMessageBox.information(self, "提示", "全局设置已成功保存到YAML文件！")
        except Exception as e:
            QMessageBox.warning(self, "警告", f"保存全局设置失败: {str(e)}")
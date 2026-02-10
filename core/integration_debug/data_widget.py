#!/usr/bin/env python3.13
"""
filename: data_widget.py
author: [spx]
email: [3123002434@mail2.gdut.edu.cn]
date: 2025-12-26
description: 用户定义主窗口的SPI数据控件。
"""
from PySide6.QtWidgets import (
        QWidget, QHBoxLayout, QVBoxLayout, QLabel, 
        QMessageBox,
        QPushButton, QLineEdit, QFrame
    )
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QSizePolicy

class Data_Widget(QWidget):
    """
        自定义列表项小部件，包含复选框、文本标签和发送按钮。
        
        Signals:
            send_clicked_signal: 点击发送按钮时触发，发送SPI数据。
            add_clicked_signal: 点击添加按钮时触发，把当前数据添加到数据组中。
            data_changed_signal: 文本编辑框内容改变时触发，包含用户数据和新文本。
    """

    send_clicked_signal = Signal(object)
    add_clicked_signal = Signal(object)
    data_changed_signal = Signal(object, str)
    name_changed_signal = Signal(object, str, str)

    def __init__(
            self, 
            parent=None, 
            data_name="", 
            data_text="", 
            type=None
        ):
        """初始化SPI数据控件.

        Args:
            parent: 父级窗口部件
            data_name (str): 数据名称
            data_text (str): 数据文本
            type (str): 控件类型，"data_group"
        """
        super().__init__(parent)

        self.data_name = data_name
        self.data_text = data_text

        self.init_ui(type)

    # ==================== UI初始化功能 ====================
    def init_ui(self, type=None):
        """初始化用户界面组件.

        Args:
            type (str): 控件类型，可以是 "data_group" 或 "test_group"
        """

        # 创建主水平布局并设置边距
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(5, 2, 10, 2)
        
        # 根据type参数决定控件行为
        if type == "data_group":
            # 添加按钮区域 - 占比 5%
            self.add_button = QPushButton("添加", self)
            self.add_button.setFixedSize(50, 25)
            self.add_button.setStyleSheet("""
                font-size: 10px;
            """)
            self.main_layout.addWidget(self.add_button, 2)  # 1/20 = 5%
            self.add_button.clicked.connect(self.add_clicked)

            # 添加竖线分割器
            self.add_vertical_separator()

            # 名称标签区域 - 占比 60%
            self.name_text = QLineEdit(f"{self.data_name}")
            self.name_text.setCursorPosition(0)  # 设置光标在开头，强制显示开头部分
            self.name_text.setStyleSheet("""
                font-family: SimSun; 
                font-weight: normal; 
                font-size: 16px;
                padding: 2px;
                border: 1px solid gray;
                border-radius: 3px;
            """)

            self.name_text.setAlignment(Qt.AlignLeft)  # 左对齐
            self.main_layout.addWidget(self.name_text, 12)  # 12/20 = 60%
            # 连接编辑完成信号，用于处理重命名和保存到YAML文件
            self.name_text.editingFinished.connect(self.handle_name_change)

            # 添加竖线分割器
            self.add_vertical_separator()

            # 可编辑文本框区域 - 占比 25%
            self.data_text_widget = QLineEdit(f"{self.data_text}")
            self.data_text_widget.setAlignment(Qt.AlignLeft)
            self.data_text_widget.setCursorPosition(0)  # 设置光标在开头，强制显示开头部分
            self.data_text_widget.setStyleSheet("""
                font-family: Times New Roman; 
                font-size: 16px;
                padding: 2px;
                border: 1px solid gray;
                border-radius: 3px;
            """)
            self.main_layout.addWidget(self.data_text_widget, 5)  # 5/20 = 25%
            self.data_text_widget.editingFinished.connect(self.edit_finish)

            # 添加竖线分割器
            self.add_vertical_separator()

            # 发送按钮区域 - 占比 10%
            self.send_button = QPushButton("发送", self)
            self.send_button.setFixedSize(60, 25)
            self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #00BFFF;
                color: white;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #0077CC;
            }
            QPushButton:pressed {
                background-color: #0077CC;
            }
            """
            )
            self.main_layout.addWidget(self.send_button, 2)  # 2/20 = 10%
            self.send_button.clicked.connect(self.send_clicked)

    def add_vertical_separator(self):
        """添加竖线分割器"""
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Plain)
        separator.setStyleSheet("QFrame { color: black; }")  # 简单的黑色细线
        self.main_layout.addWidget(separator)

    # ==================== 信号处理功能 ====================
    def send_clicked(self):
        """处理发送按钮点击事件."""
        self.send_clicked_signal.emit(getattr(self, 'user_data', None))
        self.setFocus()

    def edit_finish(self):
        """处理文本编辑完成事件."""
        text = self.data_text_widget.text().strip()

        # 只保留十六进制字符
        clean_text = ''.join(c for c in text if c in '0123456789ABCDEFabcdef')
        
        if not clean_text:
            return ""
        
        # 如果字符数为奇数，在前面补0
        if len(clean_text) % 2 != 0:
            clean_text = '0' + clean_text

        # 格式化显示，每两个字符之间添加空格
        formatted_text = ' '.join(clean_text[i:i+2] for i in range(0, len(clean_text), 2))

        self.data_text_widget.setText(formatted_text)

        # 更新内部的data_text属性
        self.data_text = formatted_text

        self.data_changed_signal.emit(getattr(self, 'user_data', None), formatted_text)
        
    def add_clicked(self):
        """处理添加按钮点击事件."""
        # 获取名称和内容数据
        name_data = self.data_name
        content_data = self.data_text.strip()
        
        # 创建包含名称和内容的数据字典
        data = {
            'name': name_data,
            'content': content_data
        }
        
        # 发射信号，传递名称和内容数据
        self.add_clicked_signal.emit(data)

    def set_user_data(self, data):
        """设置用户数据.

        Args:
            data: 要存储的用户数据
        """

        self.user_data = data

    def handle_name_change(self):
        """
        处理名称更改
        """
        new_name = self.name_text.text().strip()

        old_name  = self.data_name
        
        if not new_name:
            QMessageBox.warning(self, "警告", "名称不能为空")
            # 恢复原始名称
            self.name_text.setText(old_name)
            return

        # 更新内部的data_name属性
        self.data_name = new_name
        
        # 更新用户数据中的名称
        self.user_data.setData(Qt.UserRole, (new_name, self.data_text))

        # 传递旧名称和新名称
        self.name_changed_signal.emit(getattr(self, 'user_data', None), old_name , new_name)

    def restore_original_name(self, old_name):
        """
        恢复到原始名称
        
        Args:
            old_name: 要恢复的旧名称
        """
        # 设置标签文本为旧名称
        self.name_text.setText(old_name)
        
        # 更新内部存储的名称
        self.data_name = old_name
        
        # 更新item数据
        updated_data = (old_name, self.data_text)
        self.user_data.setData(Qt.UserRole, updated_data)
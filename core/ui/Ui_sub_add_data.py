# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_add_data.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSplitter, QTabWidget, QTextEdit,
    QWidget)

class Ui_SubForm_Data(object):
    def setupUi(self, SubForm_Data):
        if not SubForm_Data.objectName():
            SubForm_Data.setObjectName(u"SubForm_Data")
        SubForm_Data.resize(383, 169)
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        SubForm_Data.setFont(font)
        self.gridLayout_4 = QGridLayout(SubForm_Data)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, -1, 2, 2)
        self.tabWidget = QTabWidget(SubForm_Data)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_3 = QSplitter(self.tab_1)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.button_data_confirm = QPushButton(self.splitter_3)
        self.button_data_confirm.setObjectName(u"button_data_confirm")
        self.button_data_confirm.setMinimumSize(QSize(0, 40))
        self.button_data_confirm.setFont(font1)
        self.splitter_3.addWidget(self.button_data_confirm)
        self.button_data_cancel = QPushButton(self.splitter_3)
        self.button_data_cancel.setObjectName(u"button_data_cancel")
        self.button_data_cancel.setMinimumSize(QSize(0, 40))
        self.button_data_cancel.setFont(font1)
        self.splitter_3.addWidget(self.button_data_cancel)

        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(3)
        self.label_name = QLabel(self.tab_1)
        self.label_name.setObjectName(u"label_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_name.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.line_name = QLineEdit(self.tab_1)
        self.line_name.setObjectName(u"line_name")
        sizePolicy.setHeightForWidth(self.line_name.sizePolicy().hasHeightForWidth())
        self.line_name.setSizePolicy(sizePolicy)
        self.line_name.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        self.line_name.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_name)

        self.label_text = QLabel(self.tab_1)
        self.label_text.setObjectName(u"label_text")
        sizePolicy.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(sizePolicy)
        self.label_text.setMinimumSize(QSize(0, 40))
        self.label_text.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_text)

        self.line_text = QLineEdit(self.tab_1)
        self.line_text.setObjectName(u"line_text")
        sizePolicy.setHeightForWidth(self.line_text.sizePolicy().hasHeightForWidth())
        self.line_text.setSizePolicy(sizePolicy)
        self.line_text.setMinimumSize(QSize(0, 40))
        self.line_text.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_text)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherStorm))
        self.tabWidget.addTab(self.tab_1, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(11)
        self.label_9.setFont(font4)

        self.gridLayout_5.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton_add_data = QPushButton(self.tab_2)
        self.pushButton_add_data.setObjectName(u"pushButton_add_data")
        sizePolicy1.setHeightForWidth(self.pushButton_add_data.sizePolicy().hasHeightForWidth())
        self.pushButton_add_data.setSizePolicy(sizePolicy1)
        self.pushButton_add_data.setMinimumSize(QSize(0, 0))
        self.pushButton_add_data.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_add_data.setFont(font4)

        self.gridLayout_5.addWidget(self.pushButton_add_data, 4, 3, 1, 1)

        self.textEdit_formula = QTextEdit(self.tab_2)
        self.textEdit_formula.setObjectName(u"textEdit_formula")
        sizePolicy1.setHeightForWidth(self.textEdit_formula.sizePolicy().hasHeightForWidth())
        self.textEdit_formula.setSizePolicy(sizePolicy1)
        self.textEdit_formula.setMaximumSize(QSize(16777215, 25))
        self.textEdit_formula.setFont(font4)
        self.textEdit_formula.setReadOnly(True)

        self.gridLayout_5.addWidget(self.textEdit_formula, 4, 1, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_color_depth = QLabel(self.tab_2)
        self.label_color_depth.setObjectName(u"label_color_depth")
        self.label_color_depth.setMinimumSize(QSize(30, 0))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(11)
        self.label_color_depth.setFont(font5)
        self.label_color_depth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_color_depth, 0, 2, 1, 1)

        self.lineEdit_width = QLineEdit(self.tab_2)
        self.lineEdit_width.setObjectName(u"lineEdit_width")
        sizePolicy1.setHeightForWidth(self.lineEdit_width.sizePolicy().hasHeightForWidth())
        self.lineEdit_width.setSizePolicy(sizePolicy1)
        self.lineEdit_width.setFont(font5)
        self.lineEdit_width.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_width.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit_width, 0, 5, 1, 1)

        self.lineEdit_lane = QLineEdit(self.tab_2)
        self.lineEdit_lane.setObjectName(u"lineEdit_lane")
        sizePolicy1.setHeightForWidth(self.lineEdit_lane.sizePolicy().hasHeightForWidth())
        self.lineEdit_lane.setSizePolicy(sizePolicy1)
        self.lineEdit_lane.setFont(font5)
        self.lineEdit_lane.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_lane.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit_lane, 0, 1, 1, 1)

        self.lineEdit_color_depth = QLineEdit(self.tab_2)
        self.lineEdit_color_depth.setObjectName(u"lineEdit_color_depth")
        sizePolicy1.setHeightForWidth(self.lineEdit_color_depth.sizePolicy().hasHeightForWidth())
        self.lineEdit_color_depth.setSizePolicy(sizePolicy1)
        self.lineEdit_color_depth.setFont(font5)
        self.lineEdit_color_depth.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_color_depth.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit_color_depth, 0, 3, 1, 1)

        self.label_ppl = QLabel(self.tab_2)
        self.label_ppl.setObjectName(u"label_ppl")
        self.label_ppl.setMinimumSize(QSize(50, 0))
        self.label_ppl.setMaximumSize(QSize(16777215, 16777215))
        self.label_ppl.setFont(font5)
        self.label_ppl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_ppl, 0, 4, 1, 1)

        self.label_x = QLabel(self.tab_2)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setMinimumSize(QSize(10, 0))
        self.label_x.setMaximumSize(QSize(10, 31))
        self.label_x.setFont(font5)

        self.gridLayout_3.addWidget(self.label_x, 0, 6, 1, 1)

        self.label_lane = QLabel(self.tab_2)
        self.label_lane.setObjectName(u"label_lane")
        self.label_lane.setMinimumSize(QSize(35, 0))
        self.label_lane.setFont(font4)
        self.label_lane.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_lane, 0, 0, 1, 1)

        self.lineEdit_height = QLineEdit(self.tab_2)
        self.lineEdit_height.setObjectName(u"lineEdit_height")
        sizePolicy1.setHeightForWidth(self.lineEdit_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_height.setSizePolicy(sizePolicy1)
        self.lineEdit_height.setFont(font5)
        self.lineEdit_height.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_height.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit_height, 0, 7, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 4)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 1, 2, 1, 1)

        self.lineEdit_input = QLineEdit(self.tab_2)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy1)
        self.lineEdit_input.setFont(font5)
        self.lineEdit_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_input.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_input, 2, 2, 1, 2)

        self.comboBox_function = QComboBox(self.tab_2)
        self.comboBox_function.setObjectName(u"comboBox_function")
        sizePolicy1.setHeightForWidth(self.comboBox_function.sizePolicy().hasHeightForWidth())
        self.comboBox_function.setSizePolicy(sizePolicy1)
        self.comboBox_function.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_function.setFont(font4)

        self.gridLayout_5.addWidget(self.comboBox_function, 2, 0, 1, 2)

        self.label_sample = QLabel(self.tab_2)
        self.label_sample.setObjectName(u"label_sample")
        sizePolicy1.setHeightForWidth(self.label_sample.sizePolicy().hasHeightForWidth())
        self.label_sample.setSizePolicy(sizePolicy1)
        self.label_sample.setFont(font4)

        self.gridLayout_5.addWidget(self.label_sample, 3, 2, 1, 2)

        self.label_name_show = QLabel(self.tab_2)
        self.label_name_show.setObjectName(u"label_name_show")
        sizePolicy1.setHeightForWidth(self.label_name_show.sizePolicy().hasHeightForWidth())
        self.label_name_show.setSizePolicy(sizePolicy1)
        self.label_name_show.setMaximumSize(QSize(16777215, 16777215))
        self.label_name_show.setFont(font4)

        self.gridLayout_5.addWidget(self.label_name_show, 3, 0, 1, 2)

        self.gridLayout_5.setColumnMinimumWidth(0, 1)

        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(SubForm_Data)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SubForm_Data)
    # setupUi

    def retranslateUi(self, SubForm_Data):
        SubForm_Data.setWindowTitle(QCoreApplication.translate("SubForm_Data", u"Form", None))
        self.button_data_confirm.setText(QCoreApplication.translate("SubForm_Data", u"\u786e\u8ba4", None))
        self.button_data_cancel.setText(QCoreApplication.translate("SubForm_Data", u"\u53d6\u6d88", None))
        self.label_name.setText(QCoreApplication.translate("SubForm_Data", u"\u6570\u636e\u540d\u79f0", None))
        self.line_name.setText("")
        self.label_text.setText(QCoreApplication.translate("SubForm_Data", u"\u6570\u636e\u5185\u5bb9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("SubForm_Data", u"\u4e00\u822c\u6307\u4ee4", None))
        self.label_9.setText(QCoreApplication.translate("SubForm_Data", u"\u516c\u5f0f", None))
        self.label_5.setText(QCoreApplication.translate("SubForm_Data", u"\u529f\u80fd", None))
        self.pushButton_add_data.setText(QCoreApplication.translate("SubForm_Data", u"\u6dfb\u52a0", None))
        self.label_color_depth.setText(QCoreApplication.translate("SubForm_Data", u"\u8272\u6df1", None))
        self.lineEdit_width.setText(QCoreApplication.translate("SubForm_Data", u"3840", None))
        self.lineEdit_lane.setText(QCoreApplication.translate("SubForm_Data", u"2", None))
        self.lineEdit_color_depth.setText(QCoreApplication.translate("SubForm_Data", u"1024", None))
        self.label_ppl.setText(QCoreApplication.translate("SubForm_Data", u"\u5206\u8fa8\u7387", None))
        self.label_x.setText(QCoreApplication.translate("SubForm_Data", u"x", None))
        self.label_lane.setText(QCoreApplication.translate("SubForm_Data", u"\u901a\u9053", None))
        self.lineEdit_height.setText(QCoreApplication.translate("SubForm_Data", u"2160", None))
        self.label_7.setText(QCoreApplication.translate("SubForm_Data", u"\u8f93\u5165", None))
        self.label_sample.setText("")
        self.label_name_show.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SubForm_Data", u"\u5feb\u901f\u6307\u4ee4", None))
    # retranslateUi


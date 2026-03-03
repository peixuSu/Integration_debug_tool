# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from .CustomTreeWidget import CustomTreeWidget

class Ui_Application(object):
    def setupUi(self, Application):
        if not Application.objectName():
            Application.setObjectName(u"Application")
        Application.resize(755, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Application.sizePolicy().hasHeightForWidth())
        Application.setSizePolicy(sizePolicy)
        Application.setMinimumSize(QSize(0, 0))
        Application.setMaximumSize(QSize(2000, 16777215))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        Application.setFont(font)
        self.gridLayout_3 = QGridLayout(Application)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Application = QGridLayout()
        self.gridLayout_Application.setSpacing(0)
        self.gridLayout_Application.setObjectName(u"gridLayout_Application")
        self.splitter_2 = QSplitter(Application)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_2.setHandleWidth(4)
        self.splitter_2.setChildrenCollapsible(False)
        self.gridWidget_test_group = QWidget(self.splitter_2)
        self.gridWidget_test_group.setObjectName(u"gridWidget_test_group")
        self.gridWidget_test_group.setMinimumSize(QSize(200, 0))
        self.gridWidget_test_group.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_test_auto = QGridLayout(self.gridWidget_test_group)
        self.gridLayout_test_auto.setSpacing(0)
        self.gridLayout_test_auto.setObjectName(u"gridLayout_test_auto")
        self.gridLayout_test_auto.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_start = QPushButton(self.gridWidget_test_group)
        self.button_start.setObjectName(u"button_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy1)
        self.button_start.setMinimumSize(QSize(0, 30))
        self.button_start.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(10)
        self.button_start.setFont(font1)

        self.horizontalLayout.addWidget(self.button_start)

        self.button_stop = QPushButton(self.gridWidget_test_group)
        self.button_stop.setObjectName(u"button_stop")
        sizePolicy1.setHeightForWidth(self.button_stop.sizePolicy().hasHeightForWidth())
        self.button_stop.setSizePolicy(sizePolicy1)
        self.button_stop.setMinimumSize(QSize(0, 30))
        self.button_stop.setMaximumSize(QSize(16777215, 16777215))
        self.button_stop.setFont(font1)

        self.horizontalLayout.addWidget(self.button_stop)


        self.gridLayout_test_auto.addLayout(self.horizontalLayout, 4, 0, 1, 3)

        self.check_box_select_all = QCheckBox(self.gridWidget_test_group)
        self.check_box_select_all.setObjectName(u"check_box_select_all")
        sizePolicy1.setHeightForWidth(self.check_box_select_all.sizePolicy().hasHeightForWidth())
        self.check_box_select_all.setSizePolicy(sizePolicy1)
        self.check_box_select_all.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.check_box_select_all, 0, 2, 1, 1)

        self.button_add_test_group = QPushButton(self.gridWidget_test_group)
        self.button_add_test_group.setObjectName(u"button_add_test_group")
        sizePolicy1.setHeightForWidth(self.button_add_test_group.sizePolicy().hasHeightForWidth())
        self.button_add_test_group.setSizePolicy(sizePolicy1)
        self.button_add_test_group.setMaximumSize(QSize(60, 25))
        self.button_add_test_group.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.button_add_test_group, 0, 0, 1, 1)

        self.tree_group = CustomTreeWidget(self.gridWidget_test_group)
        self.tree_group.setObjectName(u"tree_group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tree_group.sizePolicy().hasHeightForWidth())
        self.tree_group.setSizePolicy(sizePolicy2)
        self.tree_group.setMinimumSize(QSize(0, 0))
        self.tree_group.setMaximumSize(QSize(350, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(10)
        self.tree_group.setFont(font2)
        self.tree_group.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tree_group.setStyleSheet(u"")
        self.tree_group.setLineWidth(1)
        self.tree_group.setAutoScrollMargin(16)
        self.tree_group.setUpdateThreshold(200)
        self.tree_group.setIndentation(20)
        self.tree_group.setColumnCount(0)
        self.tree_group.header().setMinimumSectionSize(25)
        self.tree_group.header().setDefaultSectionSize(100)

        self.gridLayout_test_auto.addWidget(self.tree_group, 1, 0, 1, 3)

        self.button_del_test_group = QPushButton(self.gridWidget_test_group)
        self.button_del_test_group.setObjectName(u"button_del_test_group")
        sizePolicy1.setHeightForWidth(self.button_del_test_group.sizePolicy().hasHeightForWidth())
        self.button_del_test_group.setSizePolicy(sizePolicy1)
        self.button_del_test_group.setMaximumSize(QSize(60, 25))
        self.button_del_test_group.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.button_del_test_group, 0, 1, 1, 1)

        self.line_number = QLineEdit(self.gridWidget_test_group)
        self.line_number.setObjectName(u"line_number")
        sizePolicy1.setHeightForWidth(self.line_number.sizePolicy().hasHeightForWidth())
        self.line_number.setSizePolicy(sizePolicy1)
        self.line_number.setMinimumSize(QSize(0, 25))
        self.line_number.setMaximumSize(QSize(16777215, 16777215))
        self.line_number.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.line_number, 3, 1, 1, 2)

        self.label_5 = QLabel(self.gridWidget_test_group)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.label_5, 2, 0, 1, 1)

        self.line_delay = QLineEdit(self.gridWidget_test_group)
        self.line_delay.setObjectName(u"line_delay")
        sizePolicy1.setHeightForWidth(self.line_delay.sizePolicy().hasHeightForWidth())
        self.line_delay.setSizePolicy(sizePolicy1)
        self.line_delay.setMinimumSize(QSize(0, 25))
        self.line_delay.setMaximumSize(QSize(16777215, 16777215))
        self.line_delay.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.line_delay, 2, 1, 1, 2)

        self.label_2 = QLabel(self.gridWidget_test_group)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font1)

        self.gridLayout_test_auto.addWidget(self.label_2, 3, 0, 1, 1)

        self.splitter_2.addWidget(self.gridWidget_test_group)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(True)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_data_group = QGridLayout(self.layoutWidget)
        self.gridLayout_data_group.setSpacing(0)
        self.gridLayout_data_group.setObjectName(u"gridLayout_data_group")
        self.gridLayout_data_group.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_data = QLineEdit(self.layoutWidget)
        self.line_data.setObjectName(u"line_data")
        sizePolicy1.setHeightForWidth(self.line_data.sizePolicy().hasHeightForWidth())
        self.line_data.setSizePolicy(sizePolicy1)
        self.line_data.setMinimumSize(QSize(0, 30))
        self.line_data.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.line_data.setFont(font3)

        self.horizontalLayout_3.addWidget(self.line_data)

        self.button_send = QPushButton(self.layoutWidget)
        self.button_send.setObjectName(u"button_send")
        sizePolicy1.setHeightForWidth(self.button_send.sizePolicy().hasHeightForWidth())
        self.button_send.setSizePolicy(sizePolicy1)
        self.button_send.setMinimumSize(QSize(0, 30))
        self.button_send.setMaximumSize(QSize(65, 16777215))
        self.button_send.setFont(font1)

        self.horizontalLayout_3.addWidget(self.button_send)

        self.button_receive = QPushButton(self.layoutWidget)
        self.button_receive.setObjectName(u"button_receive")
        sizePolicy1.setHeightForWidth(self.button_receive.sizePolicy().hasHeightForWidth())
        self.button_receive.setSizePolicy(sizePolicy1)
        self.button_receive.setMinimumSize(QSize(0, 0))
        self.button_receive.setMaximumSize(QSize(65, 30))
        self.button_receive.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_receive)

        self.label_receive_size = QLabel(self.layoutWidget)
        self.label_receive_size.setObjectName(u"label_receive_size")
        sizePolicy3.setHeightForWidth(self.label_receive_size.sizePolicy().hasHeightForWidth())
        self.label_receive_size.setSizePolicy(sizePolicy3)
        self.label_receive_size.setMinimumSize(QSize(0, 30))
        self.label_receive_size.setMaximumSize(QSize(60, 30))
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_receive_size.setFont(font4)
        self.label_receive_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_receive_size)

        self.combo_box_size = QComboBox(self.layoutWidget)
        self.combo_box_size.setObjectName(u"combo_box_size")
        sizePolicy1.setHeightForWidth(self.combo_box_size.sizePolicy().hasHeightForWidth())
        self.combo_box_size.setSizePolicy(sizePolicy1)
        self.combo_box_size.setMinimumSize(QSize(0, 30))
        self.combo_box_size.setMaximumSize(QSize(80, 30))
        self.combo_box_size.setFont(font1)

        self.horizontalLayout_3.addWidget(self.combo_box_size)


        self.gridLayout_data_group.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMaximumSize(QSize(55, 25))
        self.label_8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.line_prj_name = QLineEdit(self.layoutWidget)
        self.line_prj_name.setObjectName(u"line_prj_name")
        self.line_prj_name.setMinimumSize(QSize(70, 0))
        self.line_prj_name.setMaximumSize(QSize(90, 16777215))
        self.line_prj_name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.line_prj_name)

        self.button_new_prj = QPushButton(self.layoutWidget)
        self.button_new_prj.setObjectName(u"button_new_prj")
        sizePolicy1.setHeightForWidth(self.button_new_prj.sizePolicy().hasHeightForWidth())
        self.button_new_prj.setSizePolicy(sizePolicy1)
        self.button_new_prj.setMinimumSize(QSize(0, 25))
        self.button_new_prj.setMaximumSize(QSize(55, 16777215))
        self.button_new_prj.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_new_prj)

        self.button_import_prj = QPushButton(self.layoutWidget)
        self.button_import_prj.setObjectName(u"button_import_prj")
        sizePolicy1.setHeightForWidth(self.button_import_prj.sizePolicy().hasHeightForWidth())
        self.button_import_prj.setSizePolicy(sizePolicy1)
        self.button_import_prj.setMinimumSize(QSize(0, 25))
        self.button_import_prj.setMaximumSize(QSize(55, 16777215))
        self.button_import_prj.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_import_prj)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(45, 25))
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.combo_box_data_group = QComboBox(self.layoutWidget)
        self.combo_box_data_group.setObjectName(u"combo_box_data_group")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combo_box_data_group.sizePolicy().hasHeightForWidth())
        self.combo_box_data_group.setSizePolicy(sizePolicy5)
        self.combo_box_data_group.setMinimumSize(QSize(100, 25))
        self.combo_box_data_group.setFont(font1)

        self.horizontalLayout_2.addWidget(self.combo_box_data_group)

        self.button_rename = QPushButton(self.layoutWidget)
        self.button_rename.setObjectName(u"button_rename")
        sizePolicy1.setHeightForWidth(self.button_rename.sizePolicy().hasHeightForWidth())
        self.button_rename.setSizePolicy(sizePolicy1)
        self.button_rename.setMinimumSize(QSize(0, 25))
        self.button_rename.setMaximumSize(QSize(65, 16777215))
        self.button_rename.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_rename)

        self.button_add_data_group = QPushButton(self.layoutWidget)
        self.button_add_data_group.setObjectName(u"button_add_data_group")
        sizePolicy1.setHeightForWidth(self.button_add_data_group.sizePolicy().hasHeightForWidth())
        self.button_add_data_group.setSizePolicy(sizePolicy1)
        self.button_add_data_group.setMinimumSize(QSize(0, 25))
        self.button_add_data_group.setMaximumSize(QSize(65, 16777215))
        self.button_add_data_group.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_add_data_group)

        self.button_del_data_group = QPushButton(self.layoutWidget)
        self.button_del_data_group.setObjectName(u"button_del_data_group")
        sizePolicy1.setHeightForWidth(self.button_del_data_group.sizePolicy().hasHeightForWidth())
        self.button_del_data_group.setSizePolicy(sizePolicy1)
        self.button_del_data_group.setMinimumSize(QSize(0, 25))
        self.button_del_data_group.setMaximumSize(QSize(65, 16777215))
        self.button_del_data_group.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_del_data_group)


        self.gridLayout_data_group.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.list_data = QListWidget(self.layoutWidget)
        self.list_data.setObjectName(u"list_data")
        sizePolicy2.setHeightForWidth(self.list_data.sizePolicy().hasHeightForWidth())
        self.list_data.setSizePolicy(sizePolicy2)
        self.list_data.setMinimumSize(QSize(350, 0))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei"])
        font5.setPointSize(20)
        self.list_data.setFont(font5)

        self.horizontalLayout_4.addWidget(self.list_data)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_add = QPushButton(self.layoutWidget)
        self.button_add.setObjectName(u"button_add")
        sizePolicy1.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy1)
        self.button_add.setMinimumSize(QSize(25, 25))
        self.button_add.setMaximumSize(QSize(25, 16777215))
        self.button_add.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_add)

        self.button_det = QPushButton(self.layoutWidget)
        self.button_det.setObjectName(u"button_det")
        sizePolicy1.setHeightForWidth(self.button_det.sizePolicy().hasHeightForWidth())
        self.button_det.setSizePolicy(sizePolicy1)
        self.button_det.setMinimumSize(QSize(25, 25))
        self.button_det.setMaximumSize(QSize(25, 16777215))
        self.button_det.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_det)

        self.button_crc = QPushButton(self.layoutWidget)
        self.button_crc.setObjectName(u"button_crc")
        sizePolicy1.setHeightForWidth(self.button_crc.sizePolicy().hasHeightForWidth())
        self.button_crc.setSizePolicy(sizePolicy1)
        self.button_crc.setMinimumSize(QSize(25, 25))
        self.button_crc.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout_2.addWidget(self.button_crc)

        self.button_function_config = QPushButton(self.layoutWidget)
        self.button_function_config.setObjectName(u"button_function_config")
        sizePolicy1.setHeightForWidth(self.button_function_config.sizePolicy().hasHeightForWidth())
        self.button_function_config.setSizePolicy(sizePolicy1)
        self.button_function_config.setMinimumSize(QSize(25, 25))
        self.button_function_config.setMaximumSize(QSize(25, 25))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.button_function_config.setIcon(icon)

        self.verticalLayout_2.addWidget(self.button_function_config)

        self.button_fold_config = QPushButton(self.layoutWidget)
        self.button_fold_config.setObjectName(u"button_fold_config")
        sizePolicy1.setHeightForWidth(self.button_fold_config.sizePolicy().hasHeightForWidth())
        self.button_fold_config.setSizePolicy(sizePolicy1)
        self.button_fold_config.setMaximumSize(QSize(25, 25))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaFlash))
        self.button_fold_config.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.button_fold_config)

        self.verticalSpacer = QSpacerItem(22, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout_data_group.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.gridWidget_log = QWidget(self.splitter)
        self.gridWidget_log.setObjectName(u"gridWidget_log")
        self.gridWidget_log.setMinimumSize(QSize(0, 70))
        self.gridWidget_log.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_6 = QGridLayout(self.gridWidget_log)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.listWidget_log_normal = QListWidget(self.gridWidget_log)
        self.listWidget_log_normal.setObjectName(u"listWidget_log_normal")
        sizePolicy2.setHeightForWidth(self.listWidget_log_normal.sizePolicy().hasHeightForWidth())
        self.listWidget_log_normal.setSizePolicy(sizePolicy2)
        self.listWidget_log_normal.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamilies([u"\u5b8b\u4f53"])
        font6.setPointSize(11)
        self.listWidget_log_normal.setFont(font6)

        self.gridLayout_6.addWidget(self.listWidget_log_normal, 2, 0, 1, 1)

        self.listWidget_log = QListWidget(self.gridWidget_log)
        self.listWidget_log.setObjectName(u"listWidget_log")
        sizePolicy2.setHeightForWidth(self.listWidget_log.sizePolicy().hasHeightForWidth())
        self.listWidget_log.setSizePolicy(sizePolicy2)
        self.listWidget_log.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_log.setFont(font6)
        self.listWidget_log.setLineWidth(1)
        self.listWidget_log.setUpdateThreshold(200)
        self.listWidget_log.setSpacing(2)

        self.gridLayout_6.addWidget(self.listWidget_log, 1, 0, 1, 1)

        self.splitter.addWidget(self.gridWidget_log)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout_Application.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.widget_spi_configs = QWidget(Application)
        self.widget_spi_configs.setObjectName(u"widget_spi_configs")
        self.widget_spi_configs.setMinimumSize(QSize(0, 20))
        self.widget_spi_configs.setMaximumSize(QSize(16777215, 25))
        self.gridLayout_2 = QGridLayout(self.widget_spi_configs)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_device = QLineEdit(self.widget_spi_configs)
        self.line_device.setObjectName(u"line_device")
        sizePolicy1.setHeightForWidth(self.line_device.sizePolicy().hasHeightForWidth())
        self.line_device.setSizePolicy(sizePolicy1)
        self.line_device.setMinimumSize(QSize(0, 0))
        self.line_device.setMaximumSize(QSize(100, 16777215))
        self.line_device.setFont(font1)
        self.line_device.setReadOnly(True)

        self.gridLayout_2.addWidget(self.line_device, 0, 1, 1, 1)

        self.label_io = QLabel(self.widget_spi_configs)
        self.label_io.setObjectName(u"label_io")
        sizePolicy3.setHeightForWidth(self.label_io.sizePolicy().hasHeightForWidth())
        self.label_io.setSizePolicy(sizePolicy3)
        self.label_io.setMinimumSize(QSize(0, 0))
        self.label_io.setMaximumSize(QSize(40, 20))
        self.label_io.setFont(font1)

        self.gridLayout_2.addWidget(self.label_io, 0, 5, 1, 1)

        self.label_decive = QLabel(self.widget_spi_configs)
        self.label_decive.setObjectName(u"label_decive")
        sizePolicy3.setHeightForWidth(self.label_decive.sizePolicy().hasHeightForWidth())
        self.label_decive.setSizePolicy(sizePolicy3)
        self.label_decive.setMinimumSize(QSize(0, 0))
        self.label_decive.setMaximumSize(QSize(30, 20))
        self.label_decive.setFont(font1)

        self.gridLayout_2.addWidget(self.label_decive, 0, 0, 1, 1)

        self.label_speed = QLabel(self.widget_spi_configs)
        self.label_speed.setObjectName(u"label_speed")
        sizePolicy3.setHeightForWidth(self.label_speed.sizePolicy().hasHeightForWidth())
        self.label_speed.setSizePolicy(sizePolicy3)
        self.label_speed.setMinimumSize(QSize(0, 0))
        self.label_speed.setMaximumSize(QSize(50, 20))
        self.label_speed.setFont(font1)

        self.gridLayout_2.addWidget(self.label_speed, 0, 7, 1, 1)

        self.label_bit = QLabel(self.widget_spi_configs)
        self.label_bit.setObjectName(u"label_bit")
        sizePolicy3.setHeightForWidth(self.label_bit.sizePolicy().hasHeightForWidth())
        self.label_bit.setSizePolicy(sizePolicy3)
        self.label_bit.setMinimumSize(QSize(0, 0))
        self.label_bit.setMaximumSize(QSize(40, 20))
        self.label_bit.setFont(font1)

        self.gridLayout_2.addWidget(self.label_bit, 0, 11, 1, 1)

        self.label_clk = QLabel(self.widget_spi_configs)
        self.label_clk.setObjectName(u"label_clk")
        sizePolicy3.setHeightForWidth(self.label_clk.sizePolicy().hasHeightForWidth())
        self.label_clk.setSizePolicy(sizePolicy3)
        self.label_clk.setMinimumSize(QSize(0, 0))
        self.label_clk.setMaximumSize(QSize(30, 20))
        self.label_clk.setFont(font1)

        self.gridLayout_2.addWidget(self.label_clk, 0, 9, 1, 1)

        self.label_s_or_q = QLabel(self.widget_spi_configs)
        self.label_s_or_q.setObjectName(u"label_s_or_q")
        sizePolicy3.setHeightForWidth(self.label_s_or_q.sizePolicy().hasHeightForWidth())
        self.label_s_or_q.setSizePolicy(sizePolicy3)
        self.label_s_or_q.setMinimumSize(QSize(0, 0))
        self.label_s_or_q.setMaximumSize(QSize(40, 20))
        self.label_s_or_q.setFont(font1)

        self.gridLayout_2.addWidget(self.label_s_or_q, 0, 13, 1, 1)

        self.combo_box_s_or_q = QComboBox(self.widget_spi_configs)
        self.combo_box_s_or_q.setObjectName(u"combo_box_s_or_q")
        sizePolicy1.setHeightForWidth(self.combo_box_s_or_q.sizePolicy().hasHeightForWidth())
        self.combo_box_s_or_q.setSizePolicy(sizePolicy1)
        self.combo_box_s_or_q.setMinimumSize(QSize(0, 0))
        self.combo_box_s_or_q.setMaximumSize(QSize(100, 16777215))
        self.combo_box_s_or_q.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_s_or_q, 0, 14, 1, 1)

        self.button_refresh = QPushButton(self.widget_spi_configs)
        self.button_refresh.setObjectName(u"button_refresh")
        sizePolicy1.setHeightForWidth(self.button_refresh.sizePolicy().hasHeightForWidth())
        self.button_refresh.setSizePolicy(sizePolicy1)
        self.button_refresh.setMaximumSize(QSize(20, 16777215))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistRepeat))
        self.button_refresh.setIcon(icon2)
        self.button_refresh.setIconSize(QSize(13, 13))

        self.gridLayout_2.addWidget(self.button_refresh, 0, 2, 1, 1)

        self.combo_box_vcc = QComboBox(self.widget_spi_configs)
        self.combo_box_vcc.setObjectName(u"combo_box_vcc")
        sizePolicy1.setHeightForWidth(self.combo_box_vcc.sizePolicy().hasHeightForWidth())
        self.combo_box_vcc.setSizePolicy(sizePolicy1)
        self.combo_box_vcc.setMinimumSize(QSize(0, 0))
        self.combo_box_vcc.setMaximumSize(QSize(57, 16777215))
        self.combo_box_vcc.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_vcc, 0, 4, 1, 1)

        self.combo_box_io = QComboBox(self.widget_spi_configs)
        self.combo_box_io.setObjectName(u"combo_box_io")
        sizePolicy1.setHeightForWidth(self.combo_box_io.sizePolicy().hasHeightForWidth())
        self.combo_box_io.setSizePolicy(sizePolicy1)
        self.combo_box_io.setMinimumSize(QSize(0, 0))
        self.combo_box_io.setMaximumSize(QSize(60, 16777215))
        self.combo_box_io.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_io, 0, 6, 1, 1)

        self.combo_box_speed = QComboBox(self.widget_spi_configs)
        self.combo_box_speed.setObjectName(u"combo_box_speed")
        sizePolicy1.setHeightForWidth(self.combo_box_speed.sizePolicy().hasHeightForWidth())
        self.combo_box_speed.setSizePolicy(sizePolicy1)
        self.combo_box_speed.setMinimumSize(QSize(0, 0))
        self.combo_box_speed.setMaximumSize(QSize(80, 16777215))
        self.combo_box_speed.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_speed, 0, 8, 1, 1)

        self.combo_box_clk = QComboBox(self.widget_spi_configs)
        self.combo_box_clk.setObjectName(u"combo_box_clk")
        sizePolicy1.setHeightForWidth(self.combo_box_clk.sizePolicy().hasHeightForWidth())
        self.combo_box_clk.setSizePolicy(sizePolicy1)
        self.combo_box_clk.setMinimumSize(QSize(0, 0))
        self.combo_box_clk.setMaximumSize(QSize(100, 16777215))
        self.combo_box_clk.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_clk, 0, 10, 1, 1)

        self.label_vcc = QLabel(self.widget_spi_configs)
        self.label_vcc.setObjectName(u"label_vcc")
        sizePolicy3.setHeightForWidth(self.label_vcc.sizePolicy().hasHeightForWidth())
        self.label_vcc.setSizePolicy(sizePolicy3)
        self.label_vcc.setMinimumSize(QSize(0, 0))
        self.label_vcc.setMaximumSize(QSize(50, 20))
        self.label_vcc.setFont(font1)

        self.gridLayout_2.addWidget(self.label_vcc, 0, 3, 1, 1)

        self.combo_box_bit = QComboBox(self.widget_spi_configs)
        self.combo_box_bit.setObjectName(u"combo_box_bit")
        sizePolicy1.setHeightForWidth(self.combo_box_bit.sizePolicy().hasHeightForWidth())
        self.combo_box_bit.setSizePolicy(sizePolicy1)
        self.combo_box_bit.setMinimumSize(QSize(0, 0))
        self.combo_box_bit.setMaximumSize(QSize(60, 16777215))
        self.combo_box_bit.setFont(font1)

        self.gridLayout_2.addWidget(self.combo_box_bit, 0, 12, 1, 1)

        self.checkBox_self_test = QCheckBox(self.widget_spi_configs)
        self.checkBox_self_test.setObjectName(u"checkBox_self_test")
        sizePolicy1.setHeightForWidth(self.checkBox_self_test.sizePolicy().hasHeightForWidth())
        self.checkBox_self_test.setSizePolicy(sizePolicy1)
        self.checkBox_self_test.setFont(font1)

        self.gridLayout_2.addWidget(self.checkBox_self_test, 0, 15, 1, 1)


        self.gridLayout_Application.addWidget(self.widget_spi_configs, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_Application, 0, 0, 1, 1)


        self.retranslateUi(Application)

        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"SPI\u4e0a\u4f4d\u673a", None))
#if QT_CONFIG(tooltip)
        Application.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.button_start.setText(QCoreApplication.translate("Application", u"\u542f\u52a8", None))
        self.button_stop.setText(QCoreApplication.translate("Application", u"\u7ec8\u6b62", None))
        self.check_box_select_all.setText(QCoreApplication.translate("Application", u"\u5168\u9009", None))
        self.button_add_test_group.setText(QCoreApplication.translate("Application", u"\u6dfb\u52a0", None))
        self.button_del_test_group.setText(QCoreApplication.translate("Application", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.line_number.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.line_number.setText(QCoreApplication.translate("Application", u"1", None))
        self.label_5.setText(QCoreApplication.translate("Application", u"\u5ef6\u65f6(s)", None))
        self.label_2.setText(QCoreApplication.translate("Application", u"\u6b21\u6570", None))
        self.line_data.setText("")
        self.button_send.setText(QCoreApplication.translate("Application", u"\u53d1\u9001", None))
        self.button_receive.setText(QCoreApplication.translate("Application", u"\u53ea\u8bfb", None))
        self.label_receive_size.setText(QCoreApplication.translate("Application", u"\u53ea\u8bfb\u957f\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("Application", u"\u9879\u76ee\u540d\u79f0", None))
        self.button_new_prj.setText(QCoreApplication.translate("Application", u"\u65b0\u5efa", None))
        self.button_import_prj.setText(QCoreApplication.translate("Application", u"\u5bfc\u5165", None))
        self.label.setText(QCoreApplication.translate("Application", u"\u6570\u636e\u96c6", None))
        self.button_rename.setText(QCoreApplication.translate("Application", u"\u91cd\u547d\u540d", None))
        self.button_add_data_group.setText(QCoreApplication.translate("Application", u"\u6dfb\u52a0", None))
        self.button_del_data_group.setText(QCoreApplication.translate("Application", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.button_add.setToolTip(QCoreApplication.translate("Application", u"\u6dfb\u52a0\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.button_add.setText(QCoreApplication.translate("Application", u"+", None))
#if QT_CONFIG(tooltip)
        self.button_det.setToolTip(QCoreApplication.translate("Application", u"\u5220\u9664\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.button_det.setText(QCoreApplication.translate("Application", u"-", None))
#if QT_CONFIG(tooltip)
        self.button_crc.setToolTip(QCoreApplication.translate("Application", u"CRC\u68c0\u9a8c", None))
#endif // QT_CONFIG(tooltip)
        self.button_crc.setText(QCoreApplication.translate("Application", u"C", None))
        self.button_function_config.setText("")
        self.button_fold_config.setText("")
        self.label_io.setText(QCoreApplication.translate("Application", u"IO\u7535\u5e73", None))
        self.label_decive.setText(QCoreApplication.translate("Application", u"\u8bbe\u5907", None))
        self.label_speed.setText(QCoreApplication.translate("Application", u"SPI\u901f\u7387", None))
        self.label_bit.setText(QCoreApplication.translate("Application", u"\u4f4d\u987a\u5e8f", None))
        self.label_clk.setText(QCoreApplication.translate("Application", u"\u65f6\u949f", None))
        self.label_s_or_q.setText(QCoreApplication.translate("Application", u"S/QSPI", None))
        self.button_refresh.setText("")
        self.label_vcc.setText(QCoreApplication.translate("Application", u"VCC\u7535\u538b", None))
        self.checkBox_self_test.setText(QCoreApplication.translate("Application", u"\u81ea\u6d4b", None))
    # retranslateUi


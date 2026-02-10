# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_function_config.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(903, 258)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.tree_config = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_config.setHeaderItem(__qtreewidgetitem)
        self.tree_config.setObjectName(u"tree_config")
        font = QFont()
        font.setPointSize(10)
        self.tree_config.setFont(font)
        self.tree_config.setLineWidth(1)

        self.gridLayout_3.addWidget(self.tree_config, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 15, 0, 1, 3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.lineEdit_Horizontal_Resolution = QLineEdit(Form)
        self.lineEdit_Horizontal_Resolution.setObjectName(u"lineEdit_Horizontal_Resolution")
        self.lineEdit_Horizontal_Resolution.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Horizontal_Resolution, 7, 1, 1, 2)

        self.lineEdit_Color_Depth = QLineEdit(Form)
        self.lineEdit_Color_Depth.setObjectName(u"lineEdit_Color_Depth")
        self.lineEdit_Color_Depth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Color_Depth, 3, 1, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_Channal = QLineEdit(Form)
        self.lineEdit_Channal.setObjectName(u"lineEdit_Channal")
        self.lineEdit_Channal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Channal, 1, 1, 1, 2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_Vertical_Resolution = QLineEdit(Form)
        self.lineEdit_Vertical_Resolution.setObjectName(u"lineEdit_Vertical_Resolution")
        self.lineEdit_Vertical_Resolution.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Vertical_Resolution, 8, 1, 1, 2)

        self.lineEdit_Frame_Head = QLineEdit(Form)
        self.lineEdit_Frame_Head.setObjectName(u"lineEdit_Frame_Head")
        self.lineEdit_Frame_Head.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_Frame_Head, 0, 1, 1, 2)

        self.pushButton_Save_Edit = QPushButton(Form)
        self.pushButton_Save_Edit.setObjectName(u"pushButton_Save_Edit")

        self.gridLayout.addWidget(self.pushButton_Save_Edit, 10, 0, 1, 3)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u529f\u80fd\u914d\u7f6e\u7a97\u53e3", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6c34\u5e73\u5206\u8fa8\u7387", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Horizontal_Resolution.setToolTip(QCoreApplication.translate("Form", u"\u6c34\u5e73\u5206\u8fa8\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Horizontal_Resolution.setText(QCoreApplication.translate("Form", u"3840", None))
        self.lineEdit_Color_Depth.setText(QCoreApplication.translate("Form", u"1024", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8272\u6df1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5e27\u5934", None))
        self.lineEdit_Channal.setText(QCoreApplication.translate("Form", u"8", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5782\u76f4\u5206\u8fa8\u7387", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u901a\u9053", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Vertical_Resolution.setToolTip(QCoreApplication.translate("Form", u"\u5782\u76f4\u5206\u8fa8\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Vertical_Resolution.setText(QCoreApplication.translate("Form", u"2160", None))
        self.lineEdit_Frame_Head.setText(QCoreApplication.translate("Form", u"40", None))
        self.pushButton_Save_Edit.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9664\u5b9a\u4e49\u7684\u53d8\u91cf\u5916\uff0c\u53ef\u7528\u901a\u9053\u3001\u8272\u6df1\u3001\u6c34\u5e73\u5206\u8fa8\u7387\u3001\u5782\u76f4\u5206\u8fa8\u7387\u53c2\u4e0e\u516c\u5f0f\u8ba1\u7b97\u3002\u5982\uff1a\u516c\u5f0f\uff1a\u901a\u9053 + \u53c2\u6570</p></body></html>", None))
    # retranslateUi


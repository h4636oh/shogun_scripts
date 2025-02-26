# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scripts_selections.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 458)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton1 = QPushButton(Form)
        self.pushButton1.setObjectName(u"pushButton1")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/regex.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton1.setIcon(icon1)
        self.pushButton1.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/filter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/continue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Search", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton1.setText(QCoreApplication.translate("Form", u"Regex", None))
#if QT_CONFIG(shortcut)
        self.pushButton1.setShortcut(QCoreApplication.translate("Form", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Filter", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Form", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"SELECT ALL", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Form", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BACK", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("Form", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"CONTINUE", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("Form", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


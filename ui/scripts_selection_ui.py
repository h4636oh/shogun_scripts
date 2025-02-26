# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scripts_selection.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(700, 550))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_field = QLineEdit(Form)
        self.search_field.setObjectName(u"search_field")
        font = QFont()
        font.setPointSize(11)
        self.search_field.setFont(font)

        self.horizontalLayout.addWidget(self.search_field)

        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon)
        self.search_btn.setCheckable(False)

        self.horizontalLayout.addWidget(self.search_btn)

        self.regex_btn = QPushButton(Form)
        self.regex_btn.setObjectName(u"regex_btn")
        self.regex_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/regex.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.regex_btn.setIcon(icon1)
        self.regex_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.regex_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scripts_view = QListView(Form)
        self.scripts_view.setObjectName(u"scripts_view")
        self.scripts_view.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.scripts_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.scripts_view.setUniformItemSizes(True)

        self.verticalLayout.addWidget(self.scripts_view)

        self.select_all_btn = QPushButton(Form)
        self.select_all_btn.setObjectName(u"select_all_btn")
        self.select_all_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.select_all_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_btn = QPushButton(Form)
        self.back_btn.setObjectName(u"back_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.back_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.continue_btn = QPushButton(Form)
        self.continue_btn.setObjectName(u"continue_btn")
        self.continue_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/continue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.continue_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.continue_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_field.setText("")
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
#if QT_CONFIG(shortcut)
        self.search_btn.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.regex_btn.setText(QCoreApplication.translate("Form", u"Regex", None))
#if QT_CONFIG(shortcut)
        self.regex_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.select_all_btn.setText(QCoreApplication.translate("Form", u"SELECT ALL", None))
#if QT_CONFIG(shortcut)
        self.select_all_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.back_btn.setText(QCoreApplication.translate("Form", u"BACK", None))
#if QT_CONFIG(shortcut)
        self.back_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.continue_btn.setText(QCoreApplication.translate("Form", u"CONTINUE", None))
#if QT_CONFIG(shortcut)
        self.continue_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


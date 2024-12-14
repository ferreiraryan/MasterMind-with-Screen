# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mastermind.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: #999999;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 851, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GameText = QLabel(self.verticalLayoutWidget)
        self.GameText.setObjectName(u"GameText")
        self.GameText.setEnabled(False)
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.GameText.setFont(font)
        self.GameText.setStyleSheet(u"color:black;")

        self.verticalLayout.addWidget(self.GameText)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.Guess2 = QComboBox(self.verticalLayoutWidget)
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.addItem("")
        self.Guess2.setObjectName(u"Guess2")
        self.Guess2.setEnabled(False)
        self.Guess2.setMinimumSize(QSize(0, 150))
        self.Guess2.setAutoFillBackground(False)
        self.Guess2.setStyleSheet(u"QComboBox {\n"
"	color: white; \n"
"	background-color: #101010;\n"
"}")

        self.gridLayout.addWidget(self.Guess2, 0, 2, 1, 1)

        self.Result2 = QFrame(self.verticalLayoutWidget)
        self.Result2.setObjectName(u"Result2")
        self.Result2.setStyleSheet(u"QFrame{\n"
"background-color:black;\n"
"border-radius: 20px;\n"
"}")
        self.Result2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Result2, 1, 2, 1, 1)

        self.Guess3 = QComboBox(self.verticalLayoutWidget)
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.addItem("")
        self.Guess3.setObjectName(u"Guess3")
        self.Guess3.setEnabled(False)
        self.Guess3.setMinimumSize(QSize(0, 150))
        self.Guess3.setAutoFillBackground(False)
        self.Guess3.setStyleSheet(u"background-color: #101010; color: white;")

        self.gridLayout.addWidget(self.Guess3, 0, 3, 1, 1)

        self.Result3 = QFrame(self.verticalLayoutWidget)
        self.Result3.setObjectName(u"Result3")
        self.Result3.setMaximumSize(QSize(200, 50))
        self.Result3.setStyleSheet(u"QFrame{\n"
"background-color:black;\n"
"border-radius: 20px;\n"
"}")
        self.Result3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Result3, 1, 3, 1, 1)

        self.Guess4 = QComboBox(self.verticalLayoutWidget)
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.addItem("")
        self.Guess4.setObjectName(u"Guess4")
        self.Guess4.setEnabled(False)
        self.Guess4.setMinimumSize(QSize(200, 150))
        self.Guess4.setMaximumSize(QSize(500, 500))
        self.Guess4.setAutoFillBackground(False)
        self.Guess4.setStyleSheet(u"background-color: #101010; color: white;")

        self.gridLayout.addWidget(self.Guess4, 0, 4, 1, 1)

        self.Result4 = QFrame(self.verticalLayoutWidget)
        self.Result4.setObjectName(u"Result4")
        self.Result4.setStyleSheet(u"QFrame{\n"
"background-color:black;\n"
"border-radius: 20px;\n"
"}")
        self.Result4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Result4, 1, 4, 1, 1)

        self.Result1 = QFrame(self.verticalLayoutWidget)
        self.Result1.setObjectName(u"Result1")
        self.Result1.setMaximumSize(QSize(200, 50))
        self.Result1.setStyleSheet(u"QFrame{\n"
"background-color:black;\n"
"border-radius: 20px;\n"
"}")
        self.Result1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result1.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.Result1, 1, 0, 1, 1)

        self.Guess1 = QComboBox(self.verticalLayoutWidget)
        self.Guess1.addItem(u"None")
        self.Guess1.addItem(u"Red")
        self.Guess1.addItem(u"White")
        self.Guess1.addItem(u"Blue")
        self.Guess1.addItem(u"Yallow")
        self.Guess1.addItem(u"Orange")
        self.Guess1.addItem(u"Green")
        self.Guess1.setObjectName(u"Guess1")
        self.Guess1.setEnabled(False)
        self.Guess1.setMinimumSize(QSize(0, 150))
        self.Guess1.setAutoFillBackground(False)
        self.Guess1.setStyleSheet(u"\n"
"QComboBox {\n"
"	color: white; \n"
"	background-color: #101010;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.Guess1, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.GameButtom = QPushButton(self.widget)
        self.GameButtom.setObjectName(u"GameButtom")
        self.GameButtom.setGeometry(QRect(320, 100, 200, 70))
        self.GameButtom.setMinimumSize(QSize(200, 70))
        self.GameButtom.setMaximumSize(QSize(200, 30))
        self.GameButtom.setAcceptDrops(False)
        self.GameButtom.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Tries = QLabel(self.widget)
        self.Tries.setObjectName(u"Tries")
        self.Tries.setGeometry(QRect(210, 50, 421, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.Tries.setFont(font1)
        self.Tries.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(0, 0, 0, 148);\n"
"	border-radius:20px;\n"
"}")
        self.Tries.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.GameText.setBuddy(self.GameText)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.Guess1, self.Guess2)
        QWidget.setTabOrder(self.Guess2, self.Guess3)
        QWidget.setTabOrder(self.Guess3, self.Guess4)
        QWidget.setTabOrder(self.Guess4, self.GameButtom)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GameText.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo ao mastemind, voc\u00ea tem 10 chances de adivinhar o c\u00f3digo!", None))
        self.Guess2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.Guess2.setItemText(1, QCoreApplication.translate("MainWindow", u"Red", None))
        self.Guess2.setItemText(2, QCoreApplication.translate("MainWindow", u"White", None))
        self.Guess2.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Guess2.setItemText(4, QCoreApplication.translate("MainWindow", u"Yallow", None))
        self.Guess2.setItemText(5, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.Guess2.setItemText(6, QCoreApplication.translate("MainWindow", u"Green", None))

#if QT_CONFIG(statustip)
        self.Guess2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Guess3.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.Guess3.setItemText(1, QCoreApplication.translate("MainWindow", u"Red", None))
        self.Guess3.setItemText(2, QCoreApplication.translate("MainWindow", u"White", None))
        self.Guess3.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Guess3.setItemText(4, QCoreApplication.translate("MainWindow", u"Yallow", None))
        self.Guess3.setItemText(5, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.Guess3.setItemText(6, QCoreApplication.translate("MainWindow", u"Green", None))

#if QT_CONFIG(statustip)
        self.Guess3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Guess4.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.Guess4.setItemText(1, QCoreApplication.translate("MainWindow", u"Red", None))
        self.Guess4.setItemText(2, QCoreApplication.translate("MainWindow", u"White", None))
        self.Guess4.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Guess4.setItemText(4, QCoreApplication.translate("MainWindow", u"Yallow", None))
        self.Guess4.setItemText(5, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.Guess4.setItemText(6, QCoreApplication.translate("MainWindow", u"Green", None))

#if QT_CONFIG(statustip)
        self.Guess4.setStatusTip("")
#endif // QT_CONFIG(statustip)

#if QT_CONFIG(statustip)
        self.Guess1.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.GameButtom.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Tries.setText(QCoreApplication.translate("MainWindow", u"Clique em Start para come\u00e7ar!", None))
    # retranslateUi


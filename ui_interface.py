# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceUSYVIP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 769)
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftContainer = QCustomSlideMenu(self.centralwidget)
        self.leftContainer.setObjectName(u"leftContainer")
        self.verticalLayout = QVBoxLayout(self.leftContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 11, 0, -1)
        self.frame_11 = QFrame(self.leftContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_11.addWidget(self.label)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cbComports = QComboBox(self.frame_12)
        self.cbComports.setObjectName(u"cbComports")
        self.cbComports.setFont(font)

        self.horizontalLayout_6.addWidget(self.cbComports)

        self.btnRecarregar = QPushButton(self.frame_12)
        self.btnRecarregar.setObjectName(u"btnRecarregar")
        self.btnRecarregar.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRecarregar.setIcon(icon)
        self.btnRecarregar.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.btnRecarregar)


        self.verticalLayout_11.addWidget(self.frame_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_11.addWidget(self.label_2)

        self.cbBaudrate = QComboBox(self.frame_11)
        self.cbBaudrate.setObjectName(u"cbBaudrate")
        self.cbBaudrate.setFont(font)

        self.verticalLayout_11.addWidget(self.cbBaudrate)


        self.verticalLayout.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame = QFrame(self.leftContainer)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnConectar = QPushButton(self.frame)
        self.btnConectar.setObjectName(u"btnConectar")
        self.btnConectar.setFont(font)

        self.verticalLayout_3.addWidget(self.btnConectar)

        self.btnDeconectar = QPushButton(self.frame)
        self.btnDeconectar.setObjectName(u"btnDeconectar")
        self.btnDeconectar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnDeconectar.sizePolicy().hasHeightForWidth())
        self.btnDeconectar.setSizePolicy(sizePolicy1)
        self.btnDeconectar.setFont(font)

        self.verticalLayout_3.addWidget(self.btnDeconectar)

        self.btnReceber = QPushButton(self.frame)
        self.btnReceber.setObjectName(u"btnReceber")
        self.btnReceber.setFont(font)

        self.verticalLayout_3.addWidget(self.btnReceber)

        self.btnReset = QPushButton(self.frame)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setFont(font)

        self.verticalLayout_3.addWidget(self.btnReset)

        self.btnSalvar = QPushButton(self.frame)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setFont(font)

        self.verticalLayout_3.addWidget(self.btnSalvar)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.leftContainer, 0, Qt.AlignTop)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerConteiner = QWidget(self.mainBodyContainer)
        self.headerConteiner.setObjectName(u"headerConteiner")
        self.horizontalLayout_2 = QHBoxLayout(self.headerConteiner)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.frame_2 = QFrame(self.headerConteiner)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.headerConteiner)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.headerConteiner)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.frame_4)
        self.btnMinimize.setObjectName(u"btnMinimize")
        font2 = QFont()
        font2.setPointSize(8)
        self.btnMinimize.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimize.setIcon(icon1)
        self.btnMinimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnMinimize)

        self.btnRestore = QPushButton(self.frame_4)
        self.btnRestore.setObjectName(u"btnRestore")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRestore.setIcon(icon2)
        self.btnRestore.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnRestore)

        self.btnClose = QPushButton(self.frame_4)
        self.btnClose.setObjectName(u"btnClose")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon3)
        self.btnClose.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.headerConteiner, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.corpoConteudo = QWidget(self.mainBodyContent)
        self.corpoConteudo.setObjectName(u"corpoConteudo")
        sizePolicy3.setHeightForWidth(self.corpoConteudo.sizePolicy().hasHeightForWidth())
        self.corpoConteudo.setSizePolicy(sizePolicy3)
        self.lineChartCont = QVBoxLayout(self.corpoConteudo)
        self.lineChartCont.setObjectName(u"lineChartCont")
        self.graficoV = QFrame(self.corpoConteudo)
        self.graficoV.setObjectName(u"graficoV")
        self.graficoV.setFrameShape(QFrame.StyledPanel)
        self.graficoV.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.graficoV)
        self.gridLayout.setObjectName(u"gridLayout")

        self.lineChartCont.addWidget(self.graficoV)


        self.verticalLayout_6.addWidget(self.corpoConteudo)

        self.footerContainer = QWidget(self.mainBodyContent)
        self.footerContainer.setObjectName(u"footerContainer")
        self.verticalLayout_7 = QVBoxLayout(self.footerContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.sizeGrip)


        self.verticalLayout_6.addWidget(self.footerContainer, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PortasCOM", None))
        self.btnRecarregar.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate", None))
        self.btnConectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.btnDeconectar.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.btnReceber.setText(QCoreApplication.translate("MainWindow", u"Receber", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Resetar", None))
        self.btnSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Eletromiografia", None))
        self.btnMinimize.setText("")
        self.btnRestore.setText("")
        self.btnClose.setText("")
    # retranslateUi


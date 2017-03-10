# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portaStore.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pBtn_settings = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pBtn_settings.setObjectName(_fromUtf8("pBtn_settings"))
        self.horizontalLayout.addWidget(self.pBtn_settings)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_tdate = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_tdate.setObjectName(_fromUtf8("label_tdate"))
        self.horizontalLayout.addWidget(self.label_tdate)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pBtn_SourcesRight = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn_SourcesRight.sizePolicy().hasHeightForWidth())
        self.pBtn_SourcesRight.setSizePolicy(sizePolicy)
        self.pBtn_SourcesRight.setObjectName(_fromUtf8("pBtn_SourcesRight"))
        self.horizontalLayout.addWidget(self.pBtn_SourcesRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pBtn_applications = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pBtn_applications.setObjectName(_fromUtf8("pBtn_applications"))
        self.horizontalLayout_2.addWidget(self.pBtn_applications)
        self.pBtn_all = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pBtn_all.setMinimumSize(QtCore.QSize(32, 32))
        self.pBtn_all.setObjectName(_fromUtf8("pBtn_all"))
        self.horizontalLayout_2.addWidget(self.pBtn_all)
        self.pBtn_games = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pBtn_games.setMinimumSize(QtCore.QSize(32, 32))
        self.pBtn_games.setObjectName(_fromUtf8("pBtn_games"))
        self.horizontalLayout_2.addWidget(self.pBtn_games)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 55, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pBtn_help = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pBtn_help.setObjectName(_fromUtf8("pBtn_help"))
        self.horizontalLayout_3.addWidget(self.pBtn_help)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.num_apps_2_inUninstall = QtGui.QLCDNumber(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_apps_2_inUninstall.sizePolicy().hasHeightForWidth())
        self.num_apps_2_inUninstall.setSizePolicy(sizePolicy)
        self.num_apps_2_inUninstall.setAutoFillBackground(False)
        self.num_apps_2_inUninstall.setNumDigits(2)
        self.num_apps_2_inUninstall.setDigitCount(2)
        self.num_apps_2_inUninstall.setProperty("intValue", 0)
        self.num_apps_2_inUninstall.setObjectName(_fromUtf8("num_apps_2_inUninstall"))
        self.horizontalLayout_3.addWidget(self.num_apps_2_inUninstall)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.comboBox_accounts = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_accounts.setObjectName(_fromUtf8("comboBox_accounts"))
        self.horizontalLayout_3.addWidget(self.comboBox_accounts)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pBtn_settings, self.pBtn_SourcesRight)
        MainWindow.setTabOrder(self.pBtn_SourcesRight, self.pBtn_applications)
        MainWindow.setTabOrder(self.pBtn_applications, self.pBtn_all)
        MainWindow.setTabOrder(self.pBtn_all, self.pBtn_games)
        MainWindow.setTabOrder(self.pBtn_games, self.pBtn_help)
        MainWindow.setTabOrder(self.pBtn_help, self.comboBox_accounts)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pBtn_settings.setText(_translate("MainWindow", "Settijn", None))
        self.label_tdate.setText(_translate("MainWindow", "TextLabel", None))
        self.pBtn_SourcesRight.setText(_translate("MainWindow", "Sources", None))
        self.pBtn_applications.setText(_translate("MainWindow", "Applicatins", None))
        self.pBtn_all.setText(_translate("MainWindow", "ALL", None))
        self.pBtn_games.setText(_translate("MainWindow", "Games", None))
        self.pBtn_help.setText(_translate("MainWindow", "Help", None))


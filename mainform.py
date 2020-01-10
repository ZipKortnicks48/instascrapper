# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zipko\OneDrive\Документы\git\instascrapper\mainform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 638)
        self.buttonMedia = QtWidgets.QPushButton(Dialog)
        self.buttonMedia.setGeometry(QtCore.QRect(20, 570, 81, 23))
        self.buttonMedia.setObjectName("buttonMedia")
        self.textBoxSearch = QtWidgets.QLineEdit(Dialog)
        self.textBoxSearch.setGeometry(QtCore.QRect(390, 61, 211, 21))
        self.textBoxSearch.setObjectName("textBoxSearch")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 40, 181, 16))
        self.label.setObjectName("label")
        self.comboBoxAcc = QtWidgets.QComboBox(Dialog)
        self.comboBoxAcc.setGeometry(QtCore.QRect(20, 60, 141, 22))
        self.comboBoxAcc.setObjectName("comboBoxAcc")
        self.comboBoxAcc.addItem("")
        self.comboBoxAcc.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 201, 20))
        self.label_2.setObjectName("label_2")
        self.tableComments = QtWidgets.QTableWidget(Dialog)
        self.tableComments.setGeometry(QtCore.QRect(20, 90, 581, 471))
        self.tableComments.setObjectName("tableComments")
        self.tableComments.setColumnCount(4)
        self.tableComments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableComments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableComments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableComments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableComments.setHorizontalHeaderItem(3, item)
        self.buttonHand = QtWidgets.QPushButton(Dialog)
        self.buttonHand.setGeometry(QtCore.QRect(350, 60, 41, 23))
        self.buttonHand.setObjectName("buttonHand")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(460, 570, 141, 23))
        self.searchButton.setObjectName("searchButton")
        self.ABCchangeButton = QtWidgets.QPushButton(Dialog)
        self.ABCchangeButton.setGeometry(QtCore.QRect(20, 600, 81, 23))
        self.ABCchangeButton.setObjectName("ABCchangeButton")
        self.autoButton = QtWidgets.QPushButton(Dialog)
        self.autoButton.setGeometry(QtCore.QRect(460, 600, 141, 23))
        self.autoButton.setObjectName("autoButton")
        self.findNewComButton = QtWidgets.QPushButton(Dialog)
        self.findNewComButton.setGeometry(QtCore.QRect(270, 600, 171, 23))
        self.findNewComButton.setObjectName("findNewComButton")
        self.showCommentsButton = QtWidgets.QPushButton(Dialog)
        self.showCommentsButton.setGeometry(QtCore.QRect(270, 570, 171, 23))
        self.showCommentsButton.setObjectName("showCommentsButton")
        self.buttonStop = QtWidgets.QPushButton(Dialog)
        self.buttonStop.setGeometry(QtCore.QRect(110, 600, 75, 23))
        self.buttonStop.setObjectName("buttonStop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Форма тестовая"))
        self.buttonMedia.setText(_translate("Dialog", "Обновить БД"))
        self.label.setText(_translate("Dialog", "Введите слово для поиска"))
        self.comboBoxAcc.setItemText(0, _translate("Dialog", "igor_artamonov48"))
        self.comboBoxAcc.setItemText(1, _translate("Dialog", "zipkortnicks"))
        self.label_2.setText(_translate("Dialog", "Выберите аккаунт для отслеживания"))
        item = self.tableComments.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Дата"))
        item = self.tableComments.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Текст"))
        item = self.tableComments.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отправитель"))
        item = self.tableComments.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Ссылка на запись"))
        self.buttonHand.setText(_translate("Dialog", "🔍"))
        self.searchButton.setText(_translate("Dialog", "Поиск по новому словарю"))
        self.ABCchangeButton.setText(_translate("Dialog", "Словарь"))
        self.autoButton.setText(_translate("Dialog", "Авторежим"))
        self.findNewComButton.setText(_translate("Dialog", "Наличие новых комментариев"))
        self.showCommentsButton.setText(_translate("Dialog", "Отобразить все найденные"))
        self.buttonStop.setText(_translate("Dialog", "Остановить"))

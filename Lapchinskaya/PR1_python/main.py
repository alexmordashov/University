import math
import sys
import os
from check import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QSize


class MyWin(QtWidgets.QMainWindow):
    def init(self, parent=None):
        QtWidgets.QWidget.init(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Integral)  # функция кнопки вычислить
        self.ui.action_2.triggered.connect(self.Info)  # Beшaем на "Об автоpe" функцию Inf

    def Info(self):
        QMessageBox.about(self, "Об авторe",
                          "Програма была написана \nстудентом 2023-ФГиИБ-ПИ-1б \nБеспечаловым Артёмом")

    def Integral(self):
        self.ui.label_5.setText(' ')
        s1 = 1
        s2 = 0
        lter = 0  # Счетчик итераций
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())  # "Считываем нижнюю и верхнюю границы
        n = 4  # Число площадок (разбиений)
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())  # "Считываем" точность
        # print(a, b, eps)
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            lter += 1
            i = 0
            while i < n:
                x = a + h * (i + 0.5)
                k = math.e  (math.tan(x / 3) + 0.1)
                s2 += k * h
                i += 1
        Otvet = "\n3начение интеграла: " + str("%.3f" % (s2)) + "\nКоличество итераций: " + str(lter)
        self.ui.label_5.setText(Otvet)  # Выводим значение интеграла.
        self.Left_Integral()
        self.Rigth_Integral()

    def Left_Integral(self):
        self.ui.label_9.setText(' ')
        s1 = 1
        s2 = 0
        lter = 0  # Счетчик итераций
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())  # "Считываем нижнюю и верхнюю границы
        n = 4  # Число площадок (разбиений)
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())  # "Считываем" точность
        # print(a, b, eps)
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            lter += 1
            i = 0
            while i < n:
                x = a + h * i
                k = math.e  (math.tan(x / 3) + 0.1)
                s2 += k * h
                i += 1
        Otvet = "\n3начение интеграла: " + str("%.3f" % (s2)) + "\nКоличество итераций: " + str(lter)
        self.ui.label_9.setText(Otvet)  # Выводим значение интеграла.

    def Rigth_Integral(self):
        self.ui.label_10.setText(' ')
        s1 = 1
        s2 = 0
        lter = 0  # Счетчик итераций
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())  # "Считываем нижнюю и верхнюю границы
        n = 4  # Число площадок (разбиений)
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())  # "Считываем" точность
        # print(a, b, eps)
        while abs(s2 - s1) >= eps:
            s1 = s2
            s2 = 0
            n = n * 2
            h = (b - a) / n
            lter += 1
            i = 0
            while i < n:
                x = a + h * (i + 1)
                k = math.e ** (math.tan(x / 3) + 0.1)
                s2 += k * h
                i += 1
        Otvet = "\n3начение интеграла: " + str("%.3f" % (s2)) + "\nКоличество итераций: " + str(lter)
        self.ui.label_10.setText(Otvet)  # Выводим значение интеграла.


if name == "main":
    app = QtWidgets.QApplication(sys.argv)  # ОБЯЗАТЕЛЬНО К НАПИСАНИЮ, ДЛЯ КОРРЕКТНОЙ РАБОТЫ ПРОГРАММЫ!!!
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

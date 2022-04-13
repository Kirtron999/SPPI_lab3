from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)  # Создаём QGridLayout
        self.centralwidget.setLayout(self.grid_layout)  # Устанавливаем данное размещение в центральный виджет

        self.btn_back = QtWidgets.QPushButton(self.centralwidget)

        self.table = QtWidgets.QTableWidget(self.centralwidget)  # Создаём таблицу
        self.table.setColumnCount(7)  # Устанавливаем три колонки
        self.table.setRowCount(10)  # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["№", "Категория", "Вместимость", "Комнаты", "Удобства", "Жилец", "Стоимость"])

        # заполняем первую строку
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Люкс"))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem("4"))
        self.table.setItem(0, 3, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(0, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(0, 5, QtWidgets.QTableWidgetItem("Иванов И.И."))
        self.table.setItem(0, 6, QtWidgets.QTableWidgetItem("5500"))

        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem("Люкс"))
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem("4"))
        self.table.setItem(1, 3, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(1, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(1, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(1, 6, QtWidgets.QTableWidgetItem("5500"))

        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem("3"))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem("Полулюкс"))
        self.table.setItem(2, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(2, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(2, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(2, 5, QtWidgets.QTableWidgetItem("Иванов И.И."))
        self.table.setItem(2, 6, QtWidgets.QTableWidgetItem("4000"))

        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem("4"))
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem("Полулюкс"))
        self.table.setItem(3, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(3, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(3, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(3, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(3, 6, QtWidgets.QTableWidgetItem("4000"))

        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem("5"))
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(4, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(4, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(4, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(4, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(4, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(5, 0, QtWidgets.QTableWidgetItem("6"))
        self.table.setItem(5, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(5, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(5, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(5, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(5, 5, QtWidgets.QTableWidgetItem("Иванов И.И."))
        self.table.setItem(5, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(6, 0, QtWidgets.QTableWidgetItem("7"))
        self.table.setItem(6, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(6, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(6, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(6, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(6, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(6, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(7, 0, QtWidgets.QTableWidgetItem("8"))
        self.table.setItem(7, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(7, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(7, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(7, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(7, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(7, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(8, 0, QtWidgets.QTableWidgetItem("9"))
        self.table.setItem(8, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(8, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(8, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(8, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(8, 5, QtWidgets.QTableWidgetItem("Иванов И.И."))
        self.table.setItem(8, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(9, 0, QtWidgets.QTableWidgetItem("10"))
        self.table.setItem(9, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(9, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(9, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(9, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(9, 5, QtWidgets.QTableWidgetItem("Иванов И.И."))
        self.table.setItem(9, 6, QtWidgets.QTableWidgetItem("2500"))

        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()

        self.grid_layout.addWidget(self.btn_back, 0, 0)
        self.grid_layout.addWidget(self.table, 1, 0)  # Добавляем таблицу в сетку

        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Все номера"))
        #self.label_Date.setText(_translate("SecondWindow", "Date"))
        self.btn_back.setText(_translate("SecondWindow", "Назад"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
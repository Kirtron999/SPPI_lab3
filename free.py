from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_free(object):
    def setupUi(self, free):
        free.setObjectName("free")
        free.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(free)
        self.centralwidget.setObjectName("centralwidget")

        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)  # Создаём QGridLayout
        self.centralwidget.setLayout(self.grid_layout)  # Устанавливаем данное размещение в центральный виджет

        self.btn_back = QtWidgets.QPushButton(self.centralwidget)

        self.table = QtWidgets.QTableWidget(self.centralwidget)  # Создаём таблицу
        self.table.setColumnCount(7)  # Устанавливаем три колонки
        self.table.setRowCount(5)  # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["№", "Категория", "Вместимость", "Комнаты", "Удобства", "Жилец", "Стоимость"])

        # заполняем первую строку
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Люкс"))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem("4"))
        self.table.setItem(0, 3, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(0, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(0, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(0, 6, QtWidgets.QTableWidgetItem("5500"))

        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("4"))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem("Полулюкс"))
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(1, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(1, 4, QtWidgets.QTableWidgetItem("Кондиционер"))
        self.table.setItem(1, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(1, 6, QtWidgets.QTableWidgetItem("4000"))

        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem("5"))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(2, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(2, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(2, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(2, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(2, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem("7"))
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(3, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(3, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(3, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(3, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(3, 6, QtWidgets.QTableWidgetItem("2500"))

        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem("8"))
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem("Обычный"))
        self.table.setItem(4, 2, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(4, 3, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(4, 4, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(4, 5, QtWidgets.QTableWidgetItem(""))
        self.table.setItem(4, 6, QtWidgets.QTableWidgetItem("2500"))

        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()

        self.grid_layout.addWidget(self.btn_back, 0, 0)
        self.grid_layout.addWidget(self.table, 1, 0)  # Добавляем таблицу в сетку

        self.statusbar = QtWidgets.QStatusBar(free)
        self.statusbar.setObjectName("statusbar")
        free.setStatusBar(self.statusbar)

        free.setCentralWidget(self.centralwidget)

        self.retranslateUi(free)
        QtCore.QMetaObject.connectSlotsByName(free)

    def retranslateUi(self, free):
        _translate = QtCore.QCoreApplication.translate
        free.setWindowTitle(_translate("free", "Свободные номера"))
        #self.label_Date.setText(_translate("SecondWindow", "Date"))
        self.btn_back.setText(_translate("free", "Назад"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    free = QtWidgets.QMainWindow()
    ui = Ui_free()
    ui.setupUi(free)
    free.show()
    sys.exit(app.exec_())
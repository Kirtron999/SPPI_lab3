from PyQt5 import QtCore, QtWidgets, QtGui

class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.surname = QtWidgets.QLabel('Фамилия')
        self.name = QtWidgets.QLabel('Имя')
        self.patronymic = QtWidgets.QLabel('Отчество')
        self.date = QtWidgets.QLabel('Дата рождения')
        self.passport = QtWidgets.QLabel('Паспортные данные')
        self.indate = QtWidgets.QLabel('Дата заселения')
        self.outdate = QtWidgets.QLabel('Дата выселения')
        self.room = QtWidgets.QLabel('Номер проживания')
        self.addInfo = QtWidgets.QLabel('Дополнительная информация')

        self.surnameEdit = QtWidgets.QLineEdit()
        self.nameEdit = QtWidgets.QLineEdit()
        self.patronymicEdit = QtWidgets.QLineEdit()
        self.dateEdit = QtWidgets.QLineEdit()
        self.passportEdit = QtWidgets.QLineEdit()
        self.indateEdit = QtWidgets.QLineEdit()
        self.outdateEdit = QtWidgets.QLineEdit()
        self.roomEdit = QtWidgets.QLineEdit()
        self.addInfoEdit = QtWidgets.QTextEdit()

        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addout = QtWidgets.QPushButton(self.centralwidget)

        self.grid = QtWidgets.QGridLayout(self.centralwidget)
        self.grid.setObjectName("gridLayout")
        self.grid.setSpacing(10)

        self.grid.addWidget(self.surname, 1, 0)
        self.grid.addWidget(self.surnameEdit, 1, 1)

        self.grid.addWidget(self.name, 2, 0)
        self.grid.addWidget(self.nameEdit, 2, 1)

        self.grid.addWidget(self.patronymic, 3, 0)
        self.grid.addWidget(self.patronymicEdit, 3, 1)

        self.grid.addWidget(self.date, 4, 0)
        self.grid.addWidget(self.dateEdit, 4, 1)

        self.grid.addWidget(self.passport, 5, 0)
        self.grid.addWidget(self.passportEdit, 5, 1)

        self.grid.addWidget(self.btn_addin, 6, 0)
        self.grid.addWidget(self.indate, 6, 1)

        self.grid.addWidget(self.btn_addout, 7, 0)
        self.grid.addWidget(self.outdate, 7, 1)

        self.grid.addWidget(self.room, 8, 0)
        self.grid.addWidget(self.roomEdit, 8, 1)

        self.grid.addWidget(self.addInfo, 9, 0)
        self.grid.addWidget(self.addInfoEdit, 9, 1, 10, 1)

        self.grid.addWidget(self.btn_confirm, 13, 0)

        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        ThirdWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "Hotel app"))
        self.btn_confirm.setText(_translate("ThirdWindow", "Confirm"))
        self.btn_addin.setText(_translate("ThirdWindow", "Check-in date"))
        self.btn_addout.setText(_translate("ThirdWindow", "Check-out date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())
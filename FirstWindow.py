from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(200, 200)

        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horz = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horz.setObjectName("Layout")
        self.horz.setSpacing(10)

        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show = QtWidgets.QPushButton(self.centralwidget)
        self.btn_free = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vers = QtWidgets.QPushButton(self.centralwidget)

        self.horz.addWidget(self.btn_add, 0)
        self.horz.addWidget(self.btn_show, 1)
        self.horz.addWidget(self.btn_free, 2)
        self.horz.addWidget(self.btn_vers, 3)

        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "MainWindow"))
        self.btn_add.setText(_translate("FirstWindow", "Заселение"))
        self.btn_show.setText(_translate("FirstWindow", "Список номеров"))
        self.btn_free.setText(_translate("FirstWindow", "Свободные номера"))
        self.btn_vers.setText(_translate("FirstWindow", "Версия"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())
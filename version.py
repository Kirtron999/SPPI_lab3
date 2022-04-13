from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_version(object):
    def setupUi(self, version):
        version.setObjectName("version")
        version.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(version)
        self.centralwidget.setObjectName("centralwidget")

        self.ver = QtWidgets.QLabel('Версия:')
        self.name = QtWidgets.QLabel('Название:')
        self.about = QtWidgets.QLabel('О программе:')

        self.verText = QtWidgets.QLabel('1.1.1 se')
        self.nameText = QtWidgets.QLabel('ИС Гостиница')

        self.btn_ext = QtWidgets.QPushButton(self.centralwidget)

        self.grid = QtWidgets.QGridLayout(self.centralwidget)
        self.grid.setObjectName("gridLayout")
        self.grid.setSpacing(10)

        self.grid.addWidget(self.btn_ext, 0, 0)

        self.grid.addWidget(self.name, 1, 0)
        self.grid.addWidget(self.nameText, 1, 1)

        self.grid.addWidget(self.ver, 2, 0)
        self.grid.addWidget(self.verText, 2, 1)

        self.grid.addWidget(self.about, 3, 0)
        self.grid.addWidget(self.aboutText, 3, 1)

        self.statusbar = QtWidgets.QStatusBar(version)
        self.statusbar.setObjectName("statusbar")
        version.setStatusBar(self.statusbar)

        version.setCentralWidget(self.centralwidget)

        self.retranslateUi(version)
        QtCore.QMetaObject.connectSlotsByName(version)

    def retranslateUi(self, version):
        _translate = QtCore.QCoreApplication.translate
        version.setWindowTitle(_translate("version", "version"))
        self.btn_ext.setText(_translate("version", "На главную"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    version = QtWidgets.QMainWindow()
    ui = Ui_version()
    ui.setupUi(version)
    version.show()
    sys.exit(app.exec_())
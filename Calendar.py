from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalendarWindow(object):
    def setupUi(self, CalendarWindow):
        CalendarWindow.setObjectName("CalendarWindow")
        CalendarWindow.resize(512, 458)
        self.centralwidget = QtWidgets.QWidget(CalendarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CalendarBox = QtWidgets.QCalendarWidget(self.centralwidget)
        self.CalendarBox.setGeometry(QtCore.QRect(20, 20, 464, 289))
        self.CalendarBox.setObjectName("CalendarBox")
        self.btn_Selecteddate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Selecteddate.setGeometry(QtCore.QRect(160, 330, 181, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Selecteddate.setFont(font)
        self.btn_Selecteddate.setObjectName("btn_Selecteddate")
        CalendarWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CalendarWindow)
        self.statusbar.setObjectName("statusbar")
        CalendarWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalendarWindow)
        QtCore.QMetaObject.connectSlotsByName(CalendarWindow)

    def retranslateUi(self, CalendarWindow):
        _translate = QtCore.QCoreApplication.translate
        CalendarWindow.setWindowTitle(_translate("CalendarWindow", "Выбор даты"))
        self.btn_Selecteddate.setText(_translate("CalendarWindow", "Select"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalendarWindow = QtWidgets.QMainWindow()
    ui = Ui_CalendarWindow()
    ui.setupUi(CalendarWindow)
    CalendarWindow.show()
    sys.exit(app.exec_())
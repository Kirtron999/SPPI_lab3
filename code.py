from PyQt5 import QtWidgets
from FirstWindow import Ui_FirstWindow
from SecondWindow import Ui_SecondWindow
from ThirdWindow import Ui_ThirdWindow
from version import Ui_version
from free import Ui_free
from Calendar import Ui_CalendarWindow

class Calendar(QtWidgets.QMainWindow, Ui_CalendarWindow):                    
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

class FirstWindow(QtWidgets.QMainWindow, Ui_FirstWindow):                    
    def __init__(self):
        super(FirstWindow,self).__init__()
        self.setupUi(self)   
        self.btn_add.clicked.connect(self.open_guest_profile)
        self.btn_show.clicked.connect(self.open_rooms)
        self.btn_free.clicked.connect(self.open_free)
        self.btn_vers.clicked.connect(self.open_version)

    def open_guest_profile(self):
        self.window = ThirdWindow()
        self.window.show()
        #self.setEnabled(False)
        #self.window.setEnabled(True)

    def open_version(self):
        self.window = version()
        self.window.show()
        #self.setEnabled(False)
        #self.window.setEnabled(True)

    def open_rooms(self):
        self.window = SecondWindow()
        self.window.show()
        #self.setEnabled(False)
        #self.window.setEnabled(True)

    def open_free(self):
        self.window = free()
        self.window.show()
        #self.setEnabled(False)
        #self.window.setEnabled(True)

class SecondWindow(QtWidgets.QMainWindow, Ui_SecondWindow):                    
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.close)

class free(QtWidgets.QMainWindow, Ui_free):
    def __init__(self):
        super(free, self).__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.close)

class ThirdWindow(QtWidgets.QMainWindow, Ui_ThirdWindow):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.setupUi(self)
        self.btn_confirm.clicked.connect(self.close)
        self.btn_addin.clicked.connect(self.Open_CalendarIn)
        self.btn_addout.clicked.connect(self.Open_CalendarOut)

    def Open_CalendarIn(self):
        self.window = Calendar()
        self.window.setupUi(self.window)
        self.window.show()
        self.window.btn_Selecteddate.clicked.connect(self.CheckInDate)

    def Open_CalendarOut(self):
        self.window = Calendar()
        self.window.setupUi(self.window)
        self.window.show()
        self.window.btn_Selecteddate.clicked.connect(self.CheckOutDate)

    def CheckInDate(self):
        self.selecteddate = self.window.CalendarBox.selectedDate()
        self.indate.setText(self.selecteddate.toString("dd-MM-yyyy"))
        self.window.hide()

    def CheckOutDate(self):
        self.selecteddate = self.window.CalendarBox.selectedDate()
        self.outdate.setText(self.selecteddate.toString("dd-MM-yyyy"))
        self.window.hide()

class version(QtWidgets.QMainWindow, Ui_version):
    def __init__(self):
        super(version, self).__init__()
        self.setupUi(self)
        self.btn_ext.clicked.connect(self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = FirstWindow()    
    window.show()
    sys.exit(app.exec_())
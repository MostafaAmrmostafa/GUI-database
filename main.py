import PyQt5
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
class Wecamp (QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("try1")
        self.setGeometry(350, 200, 500, 500)
        self.ui()
        self.show

    def ui(self):
        name = QLabel("Name:", self)
        phnum = QLabel("Phone Number:", self)
        email = QLabel("Email:", self)
        password = QLabel("Passward:", self)
        track = QLabel("Track:", self)
        groub =QLabel("groub:", self)
        name.move(40, 30)
        phnum.move(40, 60)
        email.move(40, 90)
        password.move(40, 120)
        track.move(40, 150)
        groub.move(40, 220)
        textbox = QLineEdit(self)
        textbox0 = QLineEdit(self)
        textbox1 = QLineEdit(self)
        textbox2 = QLineEdit(self)
        textbox.move(130, 28)
        textbox0.move(130, 58)
        textbox1.move(130, 88)
        textbox2.move(130, 118)
        textbox.setPlaceholderText("Enter Your name")
        textbox0.setPlaceholderText("Enter Your Phone number")
        textbox1.setPlaceholderText("Enter Your Email")
        textbox2.setPlaceholderText("Enter Your Password")
        textbox2.setEchoMode(QLineEdit.Password)
        tracks = QComboBox(self)
        tracks.move(130, 150)
        tracks.addItems(["Python", "Web desian", "Networks", "Marketing"])
        radmale=QRadioButton("male", self)
        radfamale = QRadioButton("female", self)
        radmale.move(40, 190)
        radfamale.move(130, 190)
        group = QSpinBox(self)
        group.move(100,218)
        group.setRange(1, 5)
app = QApplication(sys.argv)
winshow = Wecamp()
winshow.show()
app.exec_()

import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import sqlite3

con1 = sqlite3.connect("StudentsData.db")
cursor = con1.cursor()




class Addstudent(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("try1")
        self.setGeometry(400, 300, 750, 350)
        self.uhi()

        self.layouts()
        self.show()

    def uhi(self):
        self.setStyleSheet("background-color pink ; font-size:14pt")



        self.title =QLabel ("add students")
        self.title.setStyleSheet("font-size:24pt;font family:Arial Bold; color:blue")

        self.idlbl = QLabel("National ID:", self)
        self.idEntry = QLineEdit()
        self.idEntry.setPlaceholderText("Enter student National ID ")
        self.EnglishNamelbl = QLabel("English name:")
        self.EnglishNameEntry = QLineEdit()
        self.EnglishNameEntry.setPlaceholderText("Enter student English name ")


        self.Arabicnamelbl = QLabel("Arabic name:", self)
        self.ArabicnameEntry = QLineEdit()
        self.ArabicnameEntry.setPlaceholderText("Enter student arabic name ")




        self.maillbl = QLabel("Mail:", self)
        self.mailEntry = QLineEdit()
        self.mailEntry.setPlaceholderText("Enter student Mail ")


        self.mobillbl = QLabel("Mobil:", self)
        self.mobilEntry = QLineEdit()
        self.mobilEntry.setPlaceholderText("Enter student Mobil ")


        self.gradelbl = QLabel("Grade:", self)
        self.gradeEntry = QLineEdit()
        self.gradeEntry.setPlaceholderText("Enter student Grade ")


        self.Addresslbl = QLabel("Address:", self)
        self.AddressEntry = QLineEdit()
        self.AddressEntry.setPlaceholderText("Enter student Address ")


        self.specializationlbl = QLabel("specialization:", self)
        self.specializationEntry = QLineEdit()
        self.specializationEntry.setPlaceholderText("Enter studentspecialization ")


        self.donfe=QPushButton("Add")
        self.donfe.clicked.connect(self.addstudentData)


    def addstudentData(self):
        ID = self.idEntry.text()
        EnglishName= self.EnglishNameEntry.text()
        ArabicName= self.ArabicnameEntry.text()
        Mail= self.mailEntry.text()
        Mobil= self.mobilEntry.text()
        Grade= self.gradeEntry.text()
        Specialization= self.specializationEntry.text()
        Address= self.AddressEntry.text()

        if(ID != ""):
            try:
                cursor.execute('INSERT INTO StudentsData VALUES(?,?,?,?,?,?,?,?)',(EnglishName,ArabicName,ID,Mail,Mobil,Grade,Specialization,Address));
                con1.commit()

                QMessageBox.information(self,"Success","Student has been added")
                self.gradeEntry.clear()
                self.specializationEntry.clear()
                self.mailEntry.clear()
                self.AddressEntry.clear()
                self.mobilEntry.clear()
                self.ArabicnameEntry.clear()
                self.EnglishNameEntry.clear()
                self.idEntry.clear()

            except:
                QMessageBox.information(self,"warning","student has not been added")
        else:
            QMessageBox.information(self, "warning","ID cannot be empty")

    def layouts(self):
        self.bottomlayout = QFormLayout()


        self.bottomlayout.addRow(self.title)
        self.bottomlayout.addRow(self.EnglishNamelbl,self.EnglishNameEntry)
        self.bottomlayout.addRow(self.Arabicnamelbl, self.ArabicnameEntry)
        self.bottomlayout.addRow(self.idlbl, self.idEntry)
        self.bottomlayout.addRow(self.maillbl, self.mailEntry)
        self.bottomlayout.addRow(self.mobillbl, self.mobilEntry)
        self.bottomlayout.addRow(self.gradelbl,self.gradeEntry)
        self.bottomlayout.addRow(self.specializationlbl, self.specializationEntry)
        self.bottomlayout.addRow(self.Addresslbl, self.AddressEntry)
        self.bottomlayout.addRow(self.donfe)

        self.setLayout (self.bottomlayout)


import sqlite3
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import add2
from add2 import Addstudent
con1 = sqlite3.connect("StudentsData.db")
cursor = con1.cursor()
'''
cursor.execute("CREATE TABLE  StudentsData (EnglishName VARCHAR(30) ,ArabicName VARCHAR(30), Id VARCHAR(20) PRIMARY KEY , Mail VARCHAR(30) , Mobile VARCHAR(20), grade VARCHAR(12) ,specialization VARCHAR(15), Address VARCHAR(30)) ") ;
con1.commit()
print("table created successfully")
cursor.execute("INSERT INTO  StudentsData VALUES ('yousef mohamed','يوسف محمد','22513560','yousefmohamed@gmail.com','01005546638','2','it','566')");
cursor.execute("INSERT INTO  StudentsData VALUES ('yousef hassanin','22578560','يوسف حسنين','yousefhassanin@gmail.com','01032863919','2','it','444')");
cursor.execute("INSERT INTO  StudentsData VALUES ('mostafa amr','23413560','مصطفي عمر','mostafa amr@gmail.com','01005240038','2','it','777')");
cursor.execute("INSERT INTO  StudentsData VALUES ('alaa ahmed ','23413570','الاء احمد','alaa ahmed@gmail.com','01005240038','2','it','888')");
con1.commit()
'''


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Add student")
        self.setGeometry(450,150,750,600)
        self.ui()
        self.show()

    def ui(self):
        self.mainDesign()
        self.layouts()

        self.getstudent()
        self.studentselect()
        self.deletestudent()



    def mainDesign (self):
        self.studentlist=QListWidget()
        self.studentlist.setStyleSheet("background-color:powderblue")
        self.studentlist.itemClicked.connect(self.studentselect)

        self.btwnew=QPushButton("Add")
        self.btwnew.setStyleSheet("background-color:blue ; color white")
        self.btwnew.clicked.connect(self.addstudent)

        self.btndelete=QPushButton("Delete")
        self.btndelete.setStyleSheet("background-color:orange ; color white")
        self.btndelete.clicked.connect(self.deletestudent)


    def layouts(self):
        self.mainlayout = QHBoxLayout()
        self.leftlayout = QFormLayout()
        self.rightmainlayout =QVBoxLayout()
        self.righttoplayout = QHBoxLayout()
        self.rightbottomlayout = QHBoxLayout()


        self.rightmainlayout.addLayout(self.righttoplayout)
        self.rightmainlayout.addLayout(self.rightbottomlayout)
        self.mainlayout.addLayout(self.leftlayout,40)
        self.mainlayout.addLayout(self.rightmainlayout,60)


        self.righttoplayout.addWidget(self.studentlist)
        self.rightbottomlayout.addWidget(self.btwnew)
        self.rightbottomlayout.addWidget(self.btndelete)


        self.setLayout(self.mainlayout)

    def addstudent(self):
        self.newstudent = Addstudent()
        self.close()

    def getstudent(self):

        query = "SELECT EnglishName FROM  StudentsData ORDER BY EnglishName ASC"
        students= cursor.execute(query).fetchall()
        i = 1
        for student in students:

            self.studentlist.addItem(str(i)+"-"+str(student[0]))
            i = i+1

    def studentselect(self):
        for i in reversed(range(self.leftlayout.count())):
            widget = self.leftlayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        item = self.studentlist.currentItem()
        if item is not None:
            selstudent = item.text().split("-")[1]
            query = "SELECT * FROM StudentsData WHERE EnglishName = ?"
            selectedstudent =cursor.execute(query,(selstudent,)).fetchone()
            con1.commit()
            print(selectedstudent)

            ID = QLabel(selectedstudent[0])
            EnglishName = QLabel(selectedstudent[1])
            ArabicName = QLabel(selectedstudent[2])
            mail = QLabel(selectedstudent[3])
            mobil=QLabel(selectedstudent[4])
            grade = QLabel(str(selectedstudent)[5])
            specialization=QLabel(selectedstudent[6])
            address=QLabel(selectedstudent[7])
            self.leftlayout.setVerticalSpacing(30)
            self.leftlayout.addRow("National id : ",ID)
            self.leftlayout.addRow("English Name :",EnglishName)
            self.leftlayout.addRow("Arabic Name :",ArabicName)
            self.leftlayout.addRow("Mail : ",mail)
            self.leftlayout.addRow("Mobil : ",mobil)
            self.leftlayout.addRow("Grade : ",grade)
            self.leftlayout.addRow("Specialization : ",specialization)
            self.leftlayout.addRow("Address : ",address)

    def deletestudent(self):
        item =self.studentlist.currentItem()
        if item is not None :
            delstudent = item.text().split("-")[1]
            try:
                cursor.execute("DELETE FROM StudentsData WHERE EnglishName =?",(delstudent,))
                con1.commit()
                QMessageBox.information(self,"Information", "the person has been deleted")
                self.close()
                self.main=Main()

            except:
                QMessageBox.information(self,"warning!", "student has not been delete ")
                









app = QApplication(sys.argv)
winshow = Main()
winshow.show()
app.exec_()
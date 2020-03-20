from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class child(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Teenager-Child Analysis"
        self.x=350
        self.y=100
        self.width=1000
        self.height=750
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        #DITO YUNG BACKGROUND
        photo = QImage('backtoschool-.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)

        self.button =  QPushButton("Organ Systems",self)
        self.button.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button.setGeometry(150,200,350,70)
        self.button.clicked.connect(self.organs)
        self.button2 =  QPushButton("Compute BMI",self)
        self.button2.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button2.setGeometry(150,300,350,70)
        #$self.button2.clicked.connect()
        self.button3 =  QPushButton("Health Care Tips",self)
        self.button3.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button3.setGeometry(150,400,350,70)
        #self.button3.clicked.connect(s)
        self.button4 =  QPushButton("Workout Ideas",self)
        self.button4.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button4.setGeometry(150,500,350,70)
        #self.button4.clicked.connect(self.data)

    def organs(self):
        self.organ = OrganSystems()
        self.organ.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = child()
    sys.exit(app.exec_())
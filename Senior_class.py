from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class senior(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Teenager-Senior Analysis"
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
        photo = QImage('pngtree-fresh-office-background-illustration-design-paintedcartoonfresh-backgroundoffice-backgroundillustration-image_64563.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)

        
        self.button =  QPushButton("Organ Systems",self)
        self.button.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button.setGeometry(100,200,350,70)
        self.button.clicked.connect(self.organs)
        self.button2 =  QPushButton("Compute BMI",self)
        self.button2.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button2.setGeometry(100,300,350,70)
        self.button2.clicked.connect(self.com_choice)
        self.button3 =  QPushButton("Health Care Tips",self)
        self.button3.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button3.setGeometry(100,400,350,70)
        self.button3.clicked.connect(self.H_tips)
        self.button4 =  QPushButton("Workout Ideas",self)
        self.button4.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button4.setGeometry(100,500,350,70)
        self.button4.clicked.connect(self.workout)
        
        self.show()
       
    def workout(self):
        matanda.hide(self)
        self.open = Workout_console()
        self.open.show()
    def com_choice(self):
        matanda.hide(self)
        self.open = computetanda()
        self.open.show()
    def organs(self):
        matanda.hide(self)
        self.organ = Organics()
        self.organ.show()
    def H_tips(self):
        self.matanda.hide(self)
        self.open = H_tipping()
        self.open.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = senior()
    sys.exit(app.exec_())
from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Healthcare_child(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Workout Ideas"
        self.x=350
        self.y=100
        self.width=1000
        self.height=700
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon("357-exercise-i_102408.ico"))
        photo = QImage('lawn-chair-backyard-free-vector.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('22-229057_old-man-clipart-at-getdrawings-funny-old-man.png'))
        self.doctor.setGeometry(-100,350,200,400)

        self.label = QLabel("<h1>WORKOUT IDEAS</h1>",self)
        self.label.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label.adjustSize()
        self.label.move(390,120)

        self.labelC = QLabel("<h2>CATEGORY</h2>",self)
        self.labelC.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.labelC.adjustSize()
        self.labelC.move(120,190)

        self.category = QLabel('<font size ="5"> Teenagers<br>(13-19 yrs.old)<br><br><br><br>Adults<br>(20-39 yrs.old)<br><br><br><br><br>Middle_aged<br>Adults<br>(40-59 yrs.old) </font>',self)
        self.category.setStyleSheet("text-color:black;font-weight:bold;")
        self.category.adjustSize()
        self.category.move(110,260)


        self.label1 = QLabel("<h2>HOW MUCH EACH DAY?</h2>",self)
        self.label1.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label1.adjustSize()
        self.label1.move(290,190)

        self.recom = QLabel('<font size ="4">At least 60 mins of moderate-to-vigorous-<br>intensity physical activity every day,<br>including:<br><br>Vigorous-intensity activities <br>at least 3 days a week.<br><br><br>At least 60 mins of moderate-to-vigorous-<br>intensity physical activity every day,<br>including:<br><br>Vigorous-intensity activities <br>at least 3-4 days a week.<br><br>At least 60 mins of moderate-to-vigorous-<br>intensity physical activity every day,<br>including:<br><br>Moderate-vigorous activities<br>at least 3 days a week.</font>',self)
        self.recom.setStyleSheet("text-color:black;font-weight:bold;")
        self.recom.adjustSize()
        self.recom.move(265,230)

        self.label2 = QLabel("<h2>IDEAS FOR WHAT TO DO</h2>",self)
        self.label2.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label2.adjustSize()
        self.label2.move(600,190)

        self.nutri1 = QLabel('<font size ="4">Personal fitness (a fitness class after school)<br><br>Active transportation (walking, cycling)<br><br>Competitive and non-competitive sports<br>(a game of pick-up basketball)<br><br><br>Active transportation (walking, cycling)<br>Household chores<br><br>Other ideas: canoeing, hiking, rollerblading,<br>yard work and games that require throwing<br>and catching.<br><br>Active transportation (walking, cycling)<br>Household chores<br><br>Other ideas: hiking, jogging, meditation,<br>and mind games (e.g. chess, scrabble).</font>',self)
        self.nutri1.setStyleSheet("text-color:black;font-weight:bold;")
        self.nutri1.adjustSize()
        self.nutri1.move(570,230)

        self.show()

    def paintEvent(self, event):
        linec1 = QPainter(self)
        linec1.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec1.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec1.drawRect(100, 175, 3, 405)
        
        linec2 = QPainter(self)
        linec2.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec2.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec2.drawRect(240, 175, 3, 405)

        linec3 = QPainter(self)
        linec3.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec3.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec3.drawRect(555, 175, 3, 405)

        linec4 = QPainter(self)
        linec4.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec4.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec4.drawRect(870, 175, 3, 405)

        liner1 = QPainter(self)
        liner1.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        liner1.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        liner1.drawRect(100, 175, 770, 3)

        liner2 = QPainter(self)
        liner2.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        liner2.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        liner2.drawRect(100, 220, 770, 3)

        liner3 = QPainter(self)
        liner3.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        liner3.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        liner3.drawRect(100, 340, 770, 3)
        
        liner4 = QPainter(self)
        liner4.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        liner4.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        liner4.drawRect(100, 460, 770, 3)

        liner5 = QPainter(self)
        liner5.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        liner5.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        liner5.drawRect(100, 580, 770, 3)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Healthcare_child()
    sys.exit(app.exec_())
from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Healthcare_child(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Health Care Tips"
        self.x=350
        self.y=100
        self.width=1000
        self.height=700
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('tips.png'))
        photo = QImage('vector-outdoor-jungle-gym-playground.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('smiling-child-clipart.png'))
        self.doctor.setGeometry(800,400,227,300)

        self.label = QLabel("<h1>HEALTH CARE TIPS</h1>",self)
        self.label.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label.adjustSize()
        self.label.move(380,120)

        self.labelC = QLabel("<h2>CATEGORY</h2>",self)
        self.labelC.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.labelC.adjustSize()
        self.labelC.move(160,190)

        self.category = QLabel('<font size ="5"> Infants<br>(0-2 yrs. old)<br><br><br><br><br> Pre-schoolers <br> (3-6 yrs.old) <br><br><br><br> Children<br>(6-12 yrs.old) </font>',self)
        self.category.setStyleSheet("text-color:black;font-weight:bold;")
        self.category.adjustSize()
        self.category.move(140,260)


        self.label1 = QLabel("<h2>RECOMMENDED FOODS</h2>",self)
        self.label1.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label1.adjustSize()
        self.label1.move(385,190)

        self.recom = QLabel('<font size ="4"> Vegetables:<br>Carrots, Squash,<br>Green beans,<br><br>Fruits:<br>Banana<br><br><br>Vegetables, Fruits<br><br> Meat, Egg<br><br>Lowfat-milk<br><br><br>Vegetables, Fruits<br><br>Meat, Egg<br><br>Milk, Cereal</font>',self)
        self.recom.setStyleSheet("text-color:black;font-weight:bold;")
        self.recom.adjustSize()
        self.recom.move(350,230)

        self.recom1 = QLabel('<font size ="4"> Pulses:<br>lentils, garden peas,<br>chickpeas (hummus)<br>Green beans,<br><br>Milk:<br>Breast Milk <br><br>Whole Grain Bread<br><br>Dry cereal<br><br><br><br><br>Whole Grain Bread<br><br>Yogurt, Cheese</font>',self)
        self.recom1.setStyleSheet("text-color:black;font-weight:bold;")
        self.recom1.adjustSize()
        self.recom1.move(510,230)


        self.label2 = QLabel("<h2>NUTRIENTS</h2>",self)
        self.label2.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label2.adjustSize()
        self.label2.move(700,190)

        self.nutri1 = QLabel('<font size ="4"> Potassium, Folate<br>Vitamin A<br><br>Protein, Calcium<br><br>Iron, Zinc, Magnesium<br><br><br>Vitamins<br><br>Minerals<br><br>Proteins, Fats,<br>Carbohydrates<br><br>Vitamins<br><br>Minerals<br><br>Proteins, Fats,<br>Carbohydrates</font>',self)
        self.nutri1.setStyleSheet("text-color:black;font-weight:bold;")
        self.nutri1.adjustSize()
        self.nutri1.move(680,230)

        self.show()

    def paintEvent(self, event):
        linec1 = QPainter(self)
        linec1.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec1.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec1.drawRect(100, 175, 3, 405)
        
        linec2 = QPainter(self)
        linec2.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec2.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec2.drawRect(320, 175, 3, 405)

        linec3 = QPainter(self)
        linec3.setPen(QPen(Qt.black,  0.99, Qt.SolidLine))
        linec3.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        linec3.drawRect(650, 175, 3, 405)

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
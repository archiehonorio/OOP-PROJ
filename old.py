from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class adult(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Teenager-Adult Analysis"
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
        photo = QImage('3d-empty-studio-room-show-booth-for-designers-with-spotlight-on-black-gradient-background-vector.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('adult.png'))
        self.doctor.setGeometry(300,150,400,500)
        """
        self.text = QLineEdit(self)
        self.text.setGeometry(195,150,60,30)
        self.text.setAlignment(Qt.AlignCenter)
        self.textL = QLabel("Age",self)
        self.textL.setStyleSheet("color: white; font-weight: bold;")
        self.textL.move(210,120)

        self.text1 = QLineEdit(self)
        self.text1.setGeometry(300,450,60,30)
        self.text1.setAlignment(Qt.AlignCenter)
        self.textL1 = QLabel("Height",self)
        self.textL1.setStyleSheet("color: white; font-weight: bold;")
        self.textL1.move(310,420)

        self.text2 = QLineEdit(self)
        self.text2.setGeometry(195,680,60,30)
        self.text2.setAlignment(Qt.AlignCenter)
        self.textL2 = QLabel("Weight",self)
        self.textL2.setStyleSheet("color: white; font-weight: bold;")
        self.textL2.move(205,650)
        """
        self.button =  QPushButton("Organ Systems",self)
        self.button.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button.setGeometry(325,100,350,70)
        self.button.clicked.connect(self.organs)
        self.button2 =  QPushButton("Compute BMI:",self)
        self.button2.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button2.setGeometry(375,650,250,40)
        self.button2.clicked.connect(self.compute)
        #$self.button2.clicked.connect()
        self.button3 =  QPushButton("Health Care Tips",self)
        self.button3.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button3.setGeometry(150,380,250,40)
        self.button3.clicked.connect(self.health)
        #self.button3.clicked.connect(s)
        self.button4 =  QPushButton("Workout Ideas",self)
        self.button4.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button4.setGeometry(600,380,250,40)
        self.button4.clicked.connect(self.workout)
        #self.button4.clicked.connect(self.data)
        self.show()
    def workout(self):
        self.workout = workout()
        self.workout.show()
    def organs(self):
        self.organ = OrganSystems()
        self.organ.show()
        self.computation = QPushButton
    def health(self):
        self.health = health()
        self.health.show()
    def compute(self):
        self.compute = compute()
        self.compute.show
    
class OrganSystems(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Analysis - Organ Systems"
        self.x=350
        self.y=100
        self.width=1000
        self.height=750
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        photos = QImage('shh.jpg')
        photo1 = photos.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.button =  QPushButton("Skeletal System",self)
        self.button.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #0457bf; color:white;  }""")
        self.button.setGeometry(50,50,250,40)
        self.button.clicked.connect(self.show_skeletal)
        self.button2 =  QPushButton("Endocrine System",self)
        self.button2.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button2.setGeometry(50,110,250,40)
        self.button2.clicked.connect(self.show_endocrine)
        self.button3 =  QPushButton("Nervous System",self)
        self.button3.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button3.setGeometry(50,170,250,40)
        self.button3.clicked.connect(self.show_nervous)
        self.button4 =  QPushButton("Circulatory System",self)
        self.button4.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button4.setGeometry(50,230,250,40)
        self.button4.clicked.connect(self.show_circulatory)
        self.button5 =  QPushButton("Integumentary System",self)
        self.button5.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button5.setGeometry(50,290,250,40)
        self.button5.clicked.connect(self.show_integumentary)
        self.button6 =  QPushButton("Reproductive System",self)
        self.button6.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button6.setGeometry(50,350,250,40)
        self.button6.clicked.connect(self.show_reproductive)
        self.button7 =  QPushButton("Muscular System",self)
        self.button7.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white;  }""")
        self.button7.setGeometry(50,410,250,40)
        self.button7.clicked.connect(self.show_muscular)
        self.button8 =  QPushButton("Digestive System",self)
        self.button8.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button8.setGeometry(50,470,250,40)
        self.button8.clicked.connect(self.show_digestive)
        self.button9 =  QPushButton("Respiratory System",self)
        self.button9.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button9.setGeometry(50,530,250,40)
        self.button9.clicked.connect(self.show_respiratory)
        self.button10 =  QPushButton("Urinary System",self)
        self.button10.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button10.setGeometry(50,590,250,40)
        self.button10.clicked.connect(self.show_urinary)
        self.button11 =  QPushButton("Lymphatic(Immune) System",self)
        self.button11.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button11.setGeometry(50,650,250,40)
        self.button11.clicked.connect(self.show_lymphatic)
        self.photo = QLabel(self)
        self.photo.setPixmap(QPixmap('db8d2db9c5ebcf7e4748d1370b11a146.jpg'))
        self.photo.setGeometry(350,70,620,600)
    
    def show_skeletal(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))
    def show_endocrine(self):
        self.photo.setPixmap(QPixmap("dog.jpg"))
    def show_nervous(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))
    def show_circulatory(self):
        self.photo.setPixmap(QPixmap("dog.jpg"))
    def show_muscular(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))
    def show_integumentary(self):
        self.photo.setPixmap(QPixmap("dog.jpg"))
    def show_reproductive(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))
    def show_digestive(self):
        self.photo.setPixmap(QPixmap("dog.jpg"))
    def show_respiratory(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))
    def show_urinary(self):
        self.photo.setPixmap(QPixmap("dog.jpg"))
    def show_lymphatic(self):
        self.photo.setPixmap(QPixmap("cat.jpg"))

        self.show()

class workout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appliances information")
        self.setWindowIcon(QIcon('ICON.png'))
        self.setGeometry(350,100,1000,750)

        image = QImage('background6.jpg')
        image1 = image.scaled(QSize(580,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)
            
        formLayout =QFormLayout()
        groupBox = QGroupBox()
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        groupBox.setLayout(formLayout)
        self.setLayout(layout)
        self.show()
class health(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appliances information")
        self.setWindowIcon(QIcon('ICON.png'))
        self.setGeometry(350,100,1000,750)

        image = QImage('background6.jpg')
        image1 = image.scaled(QSize(580,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)
            
        formLayout =QFormLayout()
        groupBox = QGroupBox()
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        groupBox.setLayout(formLayout)
        self.setLayout(layout)
        self.show()
class compute(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appliances information")
        self.setWindowIcon(QIcon('ICON.png'))
        self.setGeometry(350,100,1000,750)

        image = QImage('background6.jpg')
        image1 = image.scaled(QSize(580,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)
        
        formLayout =QFormLayout()
        groupBox = QGroupBox()
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        groupBox.setLayout(formLayout)
        self.setLayout(layout)
        self.show()
    def data(self):
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = adult()
    sys.exit(app.exec_())
from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from old import *
import math


class Intro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Analysis"
        self.x=350
        self.y=100
        self.width=1000
        self.height=700
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        #BACKGROUND
        photo = QImage('89918644_227961811660226_7971876158016847872_n.png')
        photo1 = photo.scaled(QSize(1000,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        #BUTTON 
        self.button = QPushButton('Click here to Start...', self)
        self.button.setStyleSheet("""background-color: transparent grey; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;""")
        self.button.setGeometry(450, 480, 300, 50)
        self.button.clicked.connect(self.open)
        self.show()
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Confirmation',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def open(self):
        Intro.hide(self)
        self.loading = loading()
        self.loading.show()

class loading(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Analysis"
        self.x=350
        self.y=100
        self.width=1000
        self.height=700     
        self.initUI()  

    def initUI(self):      
        self.loading = QProgressBar(self)
        self.loading.setStyleSheet("""QProgressBar {border: 2px groove lightgray;border-radius: 5px;text-align: center;} QProgressBar::chunk {background-color: lightblue;}""")
        self.loading.setGeometry(160, 600, 700, 25)
        self.button = QPushButton('Start', self)
        self.button.move(460, 650)
        self.button.setStyleSheet("""background-color: #D3D3D3; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;""")
        self.button.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(350, 100, 1000, 700)
        self.setWindowTitle('Human Body Analysis')
        self.setWindowIcon(QIcon('logo1.png'))

        image = QImage('90312550_848305342312426_4809600550968492032_n.png')
        image1 = image.scaled(QSize(1000,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.show()

    def timerEvent(self, e):      
        if self.step >= 100:            
            self.timer.stop()
            loading.hide(self)
            self.Main = Main()
            self.Main.show()
            return            
        self.step = self.step + 1
        self.loading.setValue(self.step)

    def doAction(self):  
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(20, self)
            self.button.setText('Stop') 
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Analysis"
        self.x=350
        self.y=100
        self.width=1000
        self.height=700
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        #DITO YUNG BACKGROUND
        photo = QImage('3.jpg')
        photo1 = photo.scaled(QSize(1000,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)

        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('doctor.png'))
        self.doctor.setGeometry(30,200,250,500)
        self.text = QLabel(self)
        self.text.setPixmap(QPixmap(''))
        self.text.setGeometry(230,10,400,400)

        self.name = QLabel("<h4>Name:</h4>",self)
        self.name.setStyleSheet("color: black; font-weight: bold;")
        self.name.move(370,250)
        self.textbox1 = QLineEdit(self)
        self.textbox1.setGeometry(370,280,250,30)
        #self.textbox1.setStyleSheet("")
        self.age = QLabel("<h4>Age:</h4>",self)
        self.age.setStyleSheet("color: black; font-weight: bold;")
        self.age.move(370,310)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setGeometry(370,340,250,30)
        #self.textbox2.setStyleSheet("")
        self.height = QLabel("<h4>Height:</h4>",self)
        self.height.setStyleSheet("color: black; font-weight: bold;")
        self.height.move(370,370)
        self.textbox3 = QLineEdit(self)
        self.textbox3.setGeometry(370,400,250,30)
        self.textbox3.setPlaceholderText("meters only")
        #self.textbox3.setStyleSheet("")        
        self.weight = QLabel("<h4>Weight:</h4>",self)
        self.weight.setStyleSheet("color: black; font-weight: bold;")
        self.weight.move(370,430)
        self.textbox4 = QLineEdit(self)
        self.textbox4.setPlaceholderText("kilograms only")
        self.textbox4.setGeometry(370,460,250,30)
        self.sex = QLabel("<h4>Sex:</h4>",self)
        self.sex.setStyleSheet("color: black; font-weight: bold;")
        self.sex.move(370,490)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setGeometry(370,520,250,30)
        #self.textbox4.setStyleSheet("")
        self.button =  QPushButton("Start",self)
        #self.button.setStyleSheet("")
        self.button.setGeometry(375,580,250,30)
        self.button.clicked.connect(self.info)
        self.show()

    def info(self):
        name = str(self.textbox1.text())
        age = int(self.textbox2.text())
        height = float(self.textbox3.text())
        weight = float(self.textbox4.text())
        sex = str(self.textbox5.text())
        ageGap = 13
        ageGap1 = 59
        ageGap2 = 60
        ageGap3 = 12
        BSA = 0.20247*(height**0.725)*(weight**0.425)
        BMI = (weight/((height)**2))*100
        self.data(name,age,height,weight,sex,ageGap,ageGap1,ageGap2,ageGap3,BMI,BSA)

    def data(self,name,age,height,weight,sex,ageGap,ageGap1,ageGap2,ageGap3,BMI,BSA):
        proceed = QMessageBox.question(self, "Submitting Data", "Confirm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if proceed == QMessageBox.Yes and name != "" and age != "" and height != "" and weight != "" and sex != "":
            dictionarydb = SqliteDict("AgeStruc.db", autocommit= True)
            ageDiff = dictionarydb.get('Age',[])
            Data = {"name":name,"age":age,"height":height,"weight":weight, "sex":sex}
            ageDiff.append(Data)
            dictionarydb['Age'] = ageDiff
            for ageStruc in dictionarydb['Age']:
                if ageStruc['age'] >= ageGap and ageStruc['age'] <= ageGap1:
                    Main.hide(self)
                    self.adult = adult()
                    self.adult.show()
                elif ageStruc['age'] >= ageGap2:
                    pass
                elif ageStruc['age'] <= ageGap3:
                    pass
            print(dictionarydb['Age'])
        elif proceed == QMessageBox.No:
            pass
        elif proceed == QMessageBox.No and name != "" and age != "" and height != "" and weight != "" and sex != "":
            pass
        elif proceed == QMessageBox.No and name != "" or age != "" or height != "" or weight != "" or sex != "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
        self.compute =compute1()
        self.compute.calculation(BMI)
        self.compute.calculation1(BSA) 
        self.compute.hide()
class compute1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computation")
        self.setWindowIcon(QIcon('ICON.png'))
        self.setGeometry(300,150,1000,750)
        photo = QImage('com.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('bmi.png'))
        self.background.setGeometry(570,200,200,200)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('bsa.png'))
        self.background.setGeometry(570,300,200,200)
    def calculation(self,BMI):

        self.bmi = QLineEdit(self)
        self.bmi.setText(f"{BMI}")
        self.bmi.setGeometry(620,320,100,20)
        self.bmi.setStyleSheet("background-color:lightgreen;")
        self.bmi.setAlignment(Qt.AlignCenter)
    def calculation1(self,BSA):

        self.bsa = QLineEdit(self)
        self.bsa.setText(f"{BSA}" )
        self.bsa.setGeometry(620,420,100,20)
        self.bsa.setAlignment(Qt.AlignCenter)
        self.bsa.setStyleSheet("background-color:lightgreen;")

        self.show()   

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

        self.button =  QPushButton("Organ Systems",self)
        self.button.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.button.setGeometry(325,100,350,70)
        self.button.clicked.connect(self.organs)
        self.button2 =  QPushButton("Compute BMI:",self)
        self.button2.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button2.setGeometry(375,650,250,40)
        self.compute1 = compute1()
        self.button2.clicked.connect(self.compute1.calculation)
        self.button2.clicked.connect(self.compute1.calculation1)
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

    def health(self):
        self.health = health()
        self.health.show()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
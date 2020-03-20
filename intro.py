from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
                    Main.hide(self)
                    self.old = matanda()
                    self.old.show()
                elif ageStruc['age'] <= ageGap3:
                    Main.hide(self)
                    self.baby = adult()
                    self.baby.show()
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
        self.bmi.setText("20.12154")
        self.bmi.setGeometry(620,320,100,20)
        self.bmi.setStyleSheet("background-color:lightgreen;")
        self.bmi.setAlignment(Qt.AlignCenter)
    def calculation1(self,BSA):

        self.bsa = QLineEdit(self)
        self.bsa.setText("30.415454")
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
        self.photo.setPixmap(QPixmap("skeletal.jpg"))
    def show_endocrine(self):
        self.photo.setPixmap(QPixmap("endocrine.jpg"))
    def show_nervous(self):
        self.photo.setPixmap(QPixmap("nervous.jpg"))
    def show_circulatory(self):
        self.photo.setPixmap(QPixmap("circulatory.jpg"))
    def show_muscular(self):
        self.photo.setPixmap(QPixmap("muscular.jpg"))
    def show_integumentary(self):
        self.photo.setPixmap(QPixmap("intergumentary.jpg"))
    def show_reproductive(self):
        self.photo.setPixmap(QPixmap("reproductive.jpg"))
    def show_digestive(self):
        self.photo.setPixmap(QPixmap("digestive.jpg"))
    def show_respiratory(self):
        self.photo.setPixmap(QPixmap("respiratory.jpg"))
    def show_urinary(self):
        self.photo.setPixmap(QPixmap("urinary.jpg"))
    def show_lymphatic(self):
        self.photo.setPixmap(QPixmap("lymphatic.jpg"))
class workout(QMainWindow):
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
class health(QMainWindow):
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
        photo = QImage('background-of-kitchen-vector-8620309.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('human-vector-png-8.png'))
        self.doctor.setGeometry(850,200,140,435)

        self.label = QLabel("<h1>HEALTH CARE TIPS</h1>",self)
        self.label.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label.adjustSize()
        self.label.move(380,120)

        self.labelC = QLabel("<h2>CATEGORY</h2>",self)
        self.labelC.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.labelC.adjustSize()
        self.labelC.move(160,190)

        self.category = QLabel('<font size ="5"> Teenagers<br>(13-19 yrs. old)<br><br><br><br>Adults<br>(20-39 yrs.old)<br><br><br><br><br>Middle_aged<br>Adults<br>(40-59 yrs.old) </font>',self)
        self.category.setStyleSheet("text-color:black;font-weight:bold;")
        self.category.adjustSize()
        self.category.move(140,260)


        self.label1 = QLabel("<h2>RECOMMENDED FOODS</h2>",self)
        self.label1.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label1.adjustSize()
        self.label1.move(385,190)

        self.recom = QLabel('<font size ="4"><br>Vegetables, Fruits, Meat<br><br>Grains, Dairy, Milk<br><br>Yogurt, Cheese<br><br><br>Vegetables, Fruits, Meat<br><br>Grains, Cereals, Dairy<br><br>Yogurt, Milk, Cheese<br><br><br><br>Vegetables, Fruits, Meat<br><br>Grains, Nuts, Cereals<br><br>Milk, Soybean, Canola oil</font>',self)
        self.recom.setStyleSheet("text-color:black;font-weight:bold;")
        self.recom.adjustSize()
        self.recom.move(350,230)


        self.label2 = QLabel("<h2>NUTRIENTS</h2>",self)
        self.label2.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label2.adjustSize()
        self.label2.move(700,190)

        self.nutri1 = QLabel('<font size ="4"> Vitamins<br><br>Minerals<br><br>Proteins, Fats,<br>Carbohydrates<br><br><br>Vitamins<br><br>Minerals<br><br>Proteins, Fats,<br>Carbohydrates<br><br>Vitamins<br><br>Minerals<br><br>Proteins, Fats, Fiber,<br>Carbohydrates</font>',self)
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

class baby(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Human Body Baby to 12 years old Analysis"
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
        self.compute1 = computeb()
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
        self.workout = workoutb()
        self.workout.show()
    def organs(self):
        self.organ = OrganB()
        self.organ.show()

    def health(self):
        self.health = htipsb()
        self.health.show()

class computeb(QMainWindow):
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
        self.bmi.setText("20.12154")
        self.bmi.setGeometry(620,320,100,20)
        self.bmi.setStyleSheet("background-color:lightgreen;")
        self.bmi.setAlignment(Qt.AlignCenter)
    def calculation1(self,BSA):

        self.bsa = QLineEdit(self)
        self.bsa.setText("30.415454")
        self.bsa.setGeometry(620,420,100,20)
        self.bsa.setAlignment(Qt.AlignCenter)
        self.bsa.setStyleSheet("background-color:lightgreen;")

        self.show()

class OrganB(QMainWindow):
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
        self.photo.setPixmap(QPixmap("skeletal.jpg"))
    def show_endocrine(self):
        self.photo.setPixmap(QPixmap("endocrine.jpg"))
    def show_nervous(self):
        self.photo.setPixmap(QPixmap("nervous.jpg"))
    def show_circulatory(self):
        self.photo.setPixmap(QPixmap("circulatory.jpg"))
    def show_muscular(self):
        self.photo.setPixmap(QPixmap("muscular.jpg"))
    def show_integumentary(self):
        self.photo.setPixmap(QPixmap("intergumentary.jpg"))
    def show_reproductive(self):
        self.photo.setPixmap(QPixmap("reproductive.jpg"))
    def show_digestive(self):
        self.photo.setPixmap(QPixmap("digestive.jpg"))
    def show_respiratory(self):
        self.photo.setPixmap(QPixmap("respiratory.jpg"))
    def show_urinary(self):
        self.photo.setPixmap(QPixmap("urinary.jpg"))
    def show_lymphatic(self):
        self.photo.setPixmap(QPixmap("lymphatic.jpg"))

class workoutb(QMainWindow):
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
        photo = QImage('hand-drawn-baby-room-with-crib-and-armchair_23-2147582108.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('sleeping-baby-clipart.png'))
        self.doctor.setGeometry(700,20,250,200)

        self.label = QLabel("<h1>WORKOUT IDEAS</h1>",self)
        self.label.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label.adjustSize()
        self.label.move(390,120)

        self.labelC = QLabel("<h2>CATEGORY</h2>",self)
        self.labelC.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.labelC.adjustSize()
        self.labelC.move(120,190)

        self.category = QLabel('<font size ="5"> Infants<br>(0-2 yrs. old)<br><br><br><br><br> Pre-schoolers <br> (3-6 yrs.old) <br><br><br><br> Children<br>(6-12 yrs.old) </font>',self)
        self.category.setStyleSheet("text-color:black;font-weight:bold;")
        self.category.adjustSize()
        self.category.move(110,260)


        self.label1 = QLabel("<h2>HOW MUCH EACH DAY?</h2>",self)
        self.label1.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label1.adjustSize()
        self.label1.move(290,190)

        self.recom = QLabel('<font size ="4"><br>Should be physically active several<br>times daily.<br>At least 30-180 minutes of tummy<br>time throughout the day.<br><br><br><br><br>They should gradually progress toward<br>at  least 60 minutes of  energetic play<br>(moderate-vigorous intensity physical<br>activity) by 5 years of age.<br><br><br><br>At least 60 mins of moderate-to-vigorous-<br>intensity physical activity every day,<br>including: Vigorous-intensity activities<br>at least 3 days a week.</font>',self)
        self.recom.setStyleSheet("text-color:black;font-weight:bold;")
        self.recom.adjustSize()
        self.recom.move(265,230)

        self.label2 = QLabel("<h2>IDEAS FOR WHAT TO DO</h2>",self)
        self.label2.setStyleSheet("background-color: lightblue; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;")
        self.label2.adjustSize()
        self.label2.move(600,190)

        self.nutri1 = QLabel('<font size ="4">Active play starts from birth, especially<br>through floor-based activities including<br>tummy-time, reaching, pushing, pulling<br>and crawling.<br<br>Activities should be fun and encourage<br>your toddler to explore new things.<br><br><br><br>Walking or running, playing tag, swimming<br>(when at least 4 yrs old), tumbling, dancing,<br>throwing and catching.<br><br><br><br><br>As they grow older, they might like to try<br>skipping and bike riding.Usually ready to<br>participate in team sports that focus on<br>skill development, equal participation and fun.</font>',self)
        self.nutri1.setStyleSheet("text-color:black;font-weight:bold;")
        self.nutri1.adjustSize()
        self.nutri1.move(575,230)

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

class htipsb(QMainWindow):
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


class matanda(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Old Age Human Body Analysis"
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
        self.doctor.setPixmap(QPixmap('matanda.jpg'))
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
        self.button2.clicked.connect(self.com_choice)
        self.button3 =  QPushButton("Health Care Tips",self)
        self.button3.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #000080; color:white; transform: }""")
        self.button3.setGeometry(150,380,250,40)
        self.button3.clicked.connect(self.H_tips)
        self.button4 =  QPushButton("Workout Ideas",self)
        self.button4.setStyleSheet("border: 2px groove white; border-radius: 5px; text-align: center; background-color: white;")
        self.button4.setGeometry(600,380,250,30)
        self.button4.clicked.connect(self.workout)
        
        self.show()
        
    def workout(self):
        self.open = Workout_console()
        self.open.show()
    def com_choice(self):
        self.open = computetanda()
        self.open.show()
    def organs(self):
        self.organ = Organics()
        self.organ.show()
    def H_tips(self):
        self.open = H_tipping()
        self.open.show()

class computetanda(QMainWindow):
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
        self.bmi.setText("20.12154")
        self.bmi.setGeometry(620,320,100,20)
        self.bmi.setStyleSheet("background-color:lightgreen;")
        self.bmi.setAlignment(Qt.AlignCenter)
    def calculation1(self,BSA):

        self.bsa = QLineEdit(self)
        self.bsa.setText("30.415454")
        self.bsa.setGeometry(620,420,100,20)
        self.bsa.setAlignment(Qt.AlignCenter)
        self.bsa.setStyleSheet("background-color:lightgreen;")

        self.show()

class Organics(QMainWindow):
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
        photos = QImage('matanda2.jpg')
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
        self.photo.setPixmap(QPixmap("skeletal.jpg"))
    def show_endocrine(self):
        self.photo.setPixmap(QPixmap("endocrine.jpg"))
    def show_nervous(self):
        self.photo.setPixmap(QPixmap("nervous.jpg"))
    def show_circulatory(self):
        self.photo.setPixmap(QPixmap("circulatory.jpg"))
    def show_muscular(self):
        self.photo.setPixmap(QPixmap("muscular.jpg"))
    def show_integumentary(self):
        self.photo.setPixmap(QPixmap("intergumentary.jpg"))
    def show_reproductive(self):
        self.photo.setPixmap(QPixmap("reproductive.jpg"))
    def show_digestive(self):
        self.photo.setPixmap(QPixmap("digestive.jpg"))
    def show_respiratory(self):
        self.photo.setPixmap(QPixmap("respiratory.jpg"))
    def show_urinary(self):
        self.photo.setPixmap(QPixmap("urinary.jpg"))
    def show_lymphatic(self):
        self.photo.setPixmap(QPixmap("lymphatic.jpg"))

class H_tipping(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title =  "Health Tips for Seniors"
        self.x = 350
        self.y = 100
        self.width = 1000
        self.height = 750
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        photos = QImage('health.jpg')
        photo1 = photos.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.pushButton = QPushButton('5 Best Health Foods for Seniors')
        self.pushButton.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #0457bf; color:white;  }""")
        self.pushButton.setGeometry(50,50,250,40)
        self.pushButton.clicked.connect(self.gtips)

        self.pushButton2 = QPushButton('5 Dangerous Foods for Seniors')
        self.pushButton.setStyleSheet("""QPushButton{border: 2px groove white; border-radius: 10px; text-align: center; font-size: 12px; background-color: #4b90c1; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 10px; text-align: center; font-size: 14px; background-color: #0457bf; color:white;  }""")
        self.pushButton.setGeometry(50,50,250,40)
        self.pushButton.clicked.connect(self.dtips)
        self.photo = QLabel(self)
        self.photo.setPixmap(QPixmap('db8d2db9c5ebcf7e4748d1370b11a146.jpg'))
        self.photo.setGeometry(350,70,620,600)

    def gtips(self):
        self.open = GoodF()
        self.open.show()

    def dtips(self):
        self.open = BadF()
        self.open.show()

class GoodF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.title =  "Good Food for Seniors"
        self.x = 350
        self.y = 100
        self.width = 1000
        self.height = 750

    def initUI(): 
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        photos = QImage('health.jpg')
        photo1 = photos.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.label = QLabel('<h4> Good Food for Seniors <h4>', self)
        self.label.setFont(QFont('Times',20, QFont.Bold))
        self.label.setStyleSheet('QLabel {color:#dedede;}')
        self.label.move(480, 50)

        self.labe2 = QLabel("<h4> Apples <h4>", self)
        self.labe2.setFont(QFont('Times', 20, QFont.Bold))
        self.labe2.setStyleSheet('QLabel {color:#dedede;}')
        self.labe2.move(480, 100)
        self.labe2.resize(120, 30)

        self.labe3 = QLabel("<h4> Shellfish <h4>", self)
        self.labe3.setFont(QFont('Times', 20, QFont.Bold))
        self.labe3.setStyleSheet('QLabel {color:#dedede;}')
        self.labe3.move(480, 250)
        self.labe3.resize(120, 30)

        self.labe4 = QLabel("<h4> Leafy green vegetables <h4>", self)
        self.labe4.setFont(QFont('Times', 20, QFont.Bold))
        self.labe4.setStyleSheet('QLabel {color:#dedede;}')
        self.labe4.move(480, 450)
        self.labe4.resize(120, 30)

        self.labe5 = QLabel("<h4> Berries and dark-skinned fruits <h4>", self)
        self.labe5.setFont(QFont('Times', 20, QFont.Bold))
        self.labe5.setStyleSheet('QLabel {color:#dedede;}')
        self.labe5.move(480, 650)
        self.labe5.resize(120, 30)

        self.labe6 = QLabel("<h4> Asparagus <h4>", self)
        self.labe6.setFont(QFont('Times', 20, QFont.Bold))
        self.labe6.setStyleSheet('QLabel {color:#dedede;}')
        self.labe6.move(480, 700)
        self.labe6.resize(120, 30)

        self.btn = QPushButton('Back', self)
        self.btn.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.btn.move(50,780)
        self.btn.resize(120, 80)
        self.btn.clicked.connect(self.balikan)
    def balikan(self):
        GoodF.hide(self)
        self.open = H_tipping()
        self.open.show()

class BadF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.title =  "Dangerous Food for Seniors"
        self.x = 350
        self.y = 100
        self.width = 1000
        self.height = 750

    def initUI(): 
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('logo1.png'))
        photos = QImage('dangold.png')
        photo1 = photos.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.label = QLabel('<h4> Dangerous Food for Seniors <h4>', self)
        self.label.setFont(QFont('Times',20, QFont.Bold))
        self.label.setStyleSheet('QLabel {color:#dedede;}')
        self.label.move(480, 50)

        self.labe2 = QLabel("<h4> Raw or undercooked eggs, meat and poultry <h4>", self)
        self.labe2.setFont(QFont('Times', 20, QFont.Bold))
        self.labe2.setStyleSheet('QLabel {color:#dedede;}')
        self.labe2.move(480, 100)
        self.labe2.resize(120, 30)

        self.labe3 = QLabel("<h4> Grapefruit <h4>", self)
        self.labe3.setFont(QFont('Times', 20, QFont.Bold))
        self.labe3.setStyleSheet('QLabel {color:#dedede;}')
        self.labe3.move(480, 250)
        self.labe3.resize(120, 30)

        self.labe4 = QLabel("<h4> High-sodium foods <h4>", self)
        self.labe4.setFont(QFont('Times', 20, QFont.Bold))
        self.labe4.setStyleSheet('QLabel {color:#dedede;}')
        self.labe4.move(480, 450)
        self.labe4.resize(120, 30)

        self.labe5 = QLabel("<h4> Sodas and sugary drinks <h4>", self)
        self.labe5.setFont(QFont('Times', 20, QFont.Bold))
        self.labe5.setStyleSheet('QLabel {color:#dedede;}')
        self.labe5.move(480, 650)
        self.labe5.resize(120, 30)

        self.labe6 = QLabel("<h4> Alcoholic beverages <h4>", self)
        self.labe6.setFont(QFont('Times', 20, QFont.Bold))
        self.labe6.setStyleSheet('QLabel {color:#dedede;}')
        self.labe6.move(480, 700)
        self.labe6.resize(120, 30)

        self.btn = QPushButton('Back', self)
        self.btn.setStyleSheet("""QPushButton{border: 3px groove white; border-radius: 30px; text-align: center; font-size: 30px; background-color: #0457bf; color:white;} QPushButton:hover {border: 2px groove white; border-radius: 20px; text-align: center; font-size: 35px; background-color: #000080; color:white; transform: }""")
        self.btn.move(50,780)
        self.btn.resize(120, 80)
        self.btn.clicked.connect(self.balik)
    def balik(self):
        BadF.hide(self)
        self.open = H_tipping()
        self.open.show()

class Workout_console(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(320, 100, 1000, 800)
        self.setWindowTitle("Workout Ideas")
        self.setWindowIcon(QIcon('logo2.png'))

        image = QImage('background1.jpg')
        image1 = image.scaled(QSize(1000,800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('anatomy1.png'))
        self.background.setGeometry(150,50,1000,200)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('anatomy2.png'))
        self.background.setGeometry(150,300,800,200)

        #Buttons
        self.MenButton = QPushButton(self)
        self.MenButton.setIcon(QIcon('man.png'))
        self.MenButton.setIconSize(QSize(80,80))
        self.MenButton.setToolTip("Senior Men Ideal Workout")
        self.MenButton.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.MenButton.move(450,450)
        self.MenButton.resize(120,120)
        self.MenButton.clicked.connect(self.ManWork)

        self.WomenButton = QPushButton('Women',self)
        self.WomenButton.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.WomenButton.move(490,570)
        self.WomenButton.setIcon(QIcon('man.png'))
        self.WomenButton.setIconSize(QSize(80,80))
        self.WomenButton.setToolTip("Senior Women Ideal Workout")
        self.WomenButton.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.WomenButton.resize(120,120)
        self.WomenButton.clicked.connect(self.WomanWork)

    def ManWork(self):
        self.man = sman()
        self.man.show()

    def WomanWork(self):
        self.wman = swman()
        self.wman.show()
    

class sman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Senior Man Ideal Workout")
        self.setWindowIcon(QIcon('man.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(1000,800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Senior Man Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Dancing", self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Strength Training", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3. Walking", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. Swimming", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Tai Chi", self)
        self.workout5.setFont(QFont('Times', 20, QFont.Bold))
        self.workout5.setStyleSheet('QLabel {color:#dedede}')
        self.workout5.move(380, 200)
        self.workout5.resize(120, 30)

        self.pushButton = QPushButton('Go Back', self)
        self.pushButton.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.pushButton.move(30,750)
        self.pushButton.setIcon(QIcon('man.png'))
        self.pushButton.setIconSize(QSize(80,80))
        self.pushButton.setToolTip("Go Back to Workout Ideas age gap selection")
        self.pushButton.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.pushButton.resize(120,120)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        sman.hide(self)
        self.open = matanda()
        self.open.show()

class swman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Senior Woman Ideal Workout")
        self.setWindowIcon(QIcon('woman.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(1000,800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Senior Woman Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Dancing", self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Strength Training", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3. Walking", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. Swimming", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Tai Chi", self)
        self.workout5.setFont(QFont('Times', 20, QFont.Bold))
        self.workout5.setStyleSheet('QLabel {color:#dedede}')
        self.workout5.move(380, 200)
        self.workout5.resize(120, 30)

        self.pushButton = QPushButton('Go Back', self)
        self.pushButton.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.pushButton.move(30,750)
        self.pushButton.setIcon(QIcon('man.png'))
        self.pushButton.setIconSize(QSize(80,80))
        self.pushButton.setToolTip("Go Back to Workout Ideas age gap selection")
        self.pushButton.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.pushButton.resize(120,120)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        sman.hide(self)
        self.open = matanda()
        self.open.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
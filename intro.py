from sqlitedict import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



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
        photo = QImage('background.jpg')
        photo1 = photo.scaled(QSize(1000,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        #BUTTON 
        self.button = QPushButton('Click here to Start...', self)
        self.button.setStyleSheet("""background-color: transparent grey; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;font-weight:bold;""")
        self.button.setGeometry(350,300,300,50)
        self.button.clicked.connect(self.open)
        self.show()

    def open(self):
        Intro.hide(self)
        self.loading = loading()
        self.loading.show()

class loading(QMainWindow):
    def __init__(self):
        super().__init__()     
        self.initUI()      
    def initUI(self):      
        self.loading = QProgressBar(self)
        self.loading.setStyleSheet("""
QProgressBar {
    border: 2px groove lightgray;
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: red;
}
""")
        self.loading.setGeometry(160, 600, 700, 25)
        self.button = QPushButton('Start', self)
        self.button.move(460, 650)
        self.button.setStyleSheet("""background-color: #D3D3D3; border-radius:10px; border-style: outset; border-width: 0.8px;border-radius: 10px; text-color:black;""")
        self.button.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(320, 100, 1000, 800)
        self.setWindowTitle('QProgressBar')

        image = QImage('loading.jpg')
        image1 = image.scaled(QSize(1000,800))
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
        photo = QImage('')
        photo1 = photo.scaled(QSize(1000,700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)

        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('doctor.png'))
        self.doctor.setGeometry(30,200,250,500)
        self.text = QLabel(self)
        self.text.setPixmap(QPixmap('text.png'))
        self.text.setGeometry(230,10,400,400)

        self.name = QLabel("<h4>Name</h4>",self)
        self.name.setStyleSheet("color: white; font-weight: bold;")
        self.name.move(360,350)
        self.textbox1 = QLineEdit(self)
        self.textbox1.setGeometry(360,380,300,30)
        #self.textbox1.setStyleSheet("")
        self.age = QLabel("<h4>Age</h4>",self)
        self.age.setStyleSheet("color: white; font-weight: bold;")
        self.age.move(360,410)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setGeometry(360,440,300,30)
        #self.textbox2.setStyleSheet("")
        self.height = QLabel("<h4>Height</h4>",self)
        self.height.setStyleSheet("color: white; font-weight: bold;")
        self.height.move(360,470)
        self.textbox3 = QLineEdit(self)
        self.textbox3.setGeometry(360,500,300,30)
        #self.textbox3.setStyleSheet("")        
        self.weight = QLabel("<h4>Weight</h4>",self)
        self.weight.setStyleSheet("color: white; font-weight: bold;")
        self.weight.move(360,530)
        self.textbox4 = QLineEdit(self)
        self.textbox4.setGeometry(360,560,300,30)
        #self.textbox4.setStyleSheet("")
        self.button =  QPushButton("Start",self)
        #self.button.setStyleSheet("")
        self.button.setGeometry(380,600,250,30)
        self.button.clicked.connect(self.data)
        self.show()
    def data(self):
        #accID = int(self.textbox5.text())
        name = str(self.textbox1.text())
        age = int(self.textbox2.text())
        height = int(self.textbox3.text())
        weight = int(self.textbox4.text())
        ageGap = 13
        ageGap1 = 59
        ageGap2 = 60
        ageGap3 = 12
        dictionarydb = SqliteDict("AgeStruc.db", autocommit= True)
        ageDiff = dictionarydb.get('Age',[])
        Data = {"name":name,"age":age,"height":height,"weight":weight}
        ageDiff.append(Data)
        dictionarydb['Age'] = ageDiff  
        for ageStruc in dictionarydb['Age']:
            if ageStruc['age'] >= ageGap and ageStruc['age'] <= ageGap1:
                Main.hide(self)
                self.adult = adult()
                self.adult.show()
            elif ageStruc['age'] >= ageGap2:
                Main.hide(self)
                self.old_age = matanda()
                self.old_age.show()
            elif ageStruc['age'] <= ageGap3:
                Main.hide(self)
                self.old_age = teen()
                self.old_age.show()
        print(dictionarydb['Age'])
"""
        self.id = QLabel("<h4>Account ID</h4>",self)
        self.id.setStyleSheet("color: white; font-weight: bold;")
        self.id.move(700,350)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setGeometry(700,380,100,30)
        #self.textbox5.setStyleSheet("")

        self.button1 = QPushButton("Account",self)
        self.button1.setGeometry(600,300,100,30)
        self.button1.clicked.connect(self.acc1)
    def acc1(self):
        self.acc1 = acc1()
        self.acc1.show()

    class acc1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Account')
        self.setWindowIcon(QIcon('ICON.png'))
        self.resize(300,120)
        self.background = QLabel(self)
        #background
        self.background.setPixmap(QPixmap(''))
        self.background.setGeometry(1,1,900,700)
        layout = QGridLayout()
        accountL =QLabel('<font size ="3"> Account ID </font>')
        accountL.setStyleSheet("color:black; font-weight: bold;")
        self.account = QLineEdit()
        self.account.setPlaceholderText('Please enter your account ID...')
        self.button = QPushButton('proceed')
        self.button.setStyleSheet(""background-color: #FFDF00; border-radius:5px; border-style: outset; border-width: 0.8px;border-radius: 5px; text-color:black;")
        self.button.clicked.connect(self.accounts)
        self.button1 = QPushButton('Close')
        self.button1.setStyleSheet(""background-color: #FFDF00; border-radius:5px; border-style: outset; border-width: 0.8px;border-radius: 5px; text-color:black;")
        self.button1.clicked.connect(self.close)
        layout.addWidget(self.account,0,1)
        layout.addWidget(accountL, 0, 0)
        layout.addWidget(self.button,2,0)
        layout.addWidget(self.button1,3,0)
        self.setLayout(layout)
        self.show()
    def close(self):
        acc1.hide(self)
    def accounts(self):
        accID1 = self.account.text()
        accID = accID1.astype(int)
        dictionarydb = SqliteDict("AgeStruc.db", autocommit= True)
        ageDiff = dictionarydb.get('Age',[])
        dictionarydb['Age'] = ageDiff
        for account in dictionarydb:
            if account['accID'] == accID:
                print("gago")
            else:
                pass 
            #QMessageBOx       
    """
class teen(QMainWindow):
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
        photo = QImage('')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('adult.png'))
        self.doctor.setGeometry(30,200,400,500)
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
        self.button4.setStyleSheet("border: 2px groove white; border-radius: 5px; text-align: center; background-color: white;")
        self.button4.setGeometry(600,380,250,30)
        self.button4.clicked.connect(self.workout)

        self.computation = QPushButton
        self.show()

    def workout(self):
        self.hide(self)
        self.open = Workout_console()
        self.open.show()

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
        photo = QImage('')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('adult.png'))
        self.doctor.setGeometry(30,200,400,500)
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
        self.button4.setStyleSheet("border: 2px groove white; border-radius: 5px; text-align: center; background-color: white;")
        self.button4.setGeometry(600,380,250,30)
        self.button4.clicked.connect(self.workout)

        self.computation = QPushButton
        self.show()

    def workout(self):
        self.hide(self)
        self.open = Workout_console()
        self.open.show()

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
        photo = QImage('background1.jpg')
        photo1 = photo.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(photo1))
        self.setPalette(palette)
        self.doctor = QLabel(self)
        self.doctor.setPixmap(QPixmap('matanda2.jpg'))
        self.doctor.setGeometry(30,200,400,500)
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


        self.computation = QPushButton('Computation', self)
        self.computation.setStyleSheet("""background-color: #FFDF00; border-radius:5px; border-style: outset; border-width: 0.8px;border-radius: 5px; text-color:black;""")
        self.computation.clicked.connect(self.com_choice) #connected sa def com_choice whichc leads to class window computations
        
        self.button4 =  QPushButton("Workout Ideas",self)
        self.button4.setStyleSheet("border: 2px groove white; border-radius: 5px; text-align: center; background-color: white;")
        self.button4.setGeometry(600,380,250,30)
        self.button4.clicked.connect(self.workout)

        def workout(self):
            self.hide(self)
            self.open = Workout_console()
            self.open.show()
        
        self.show()

class Workout_console(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(320, 100, 1000, 800)
        self.setWindowTitle("Workout Ideas")
        self.setWindowIcon(QIcon('logo2.png'))

        image = QImage('background1.jpg')
        image1 = image.scaled(QSize(100,800))
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

        self.MenButton2 = QPushButton('Adult Men', self)
        self.MenButton2.setIcon(QIcon('man.png'))
        self.MenButton2.setIconSize(QSize(80,80))
        self.MenButton2.setToolTip("Adult Men Ideal Workout")
        self.MenButton2.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.MenButton2.move(250,450)
        self.MenButton2.resize(120,120)
        self.MenButton2.clicked.connect(self.ManWork2)

        self.WomenButton2 = QPushButton('Adult Women',self)
        self.WomenButton2.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.WomenButton2.move(290,570)
        self.WomenButton2.setIcon(QIcon('man.png'))
        self.WomenButton2.setIconSize(QSize(80,80))
        self.WomenButton2.setToolTip("Adult Women Ideal Workout")
        self.WomenButton2.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.WomenButton2.resize(120,120)
        self.WomenButton2.clicked.connect(self.WomanWork2)

        self.MenButton3 = QPushButton('Teen Man', self)
        self.MenButton3.setIcon(QIcon('man.png'))
        self.MenButton3.setIconSize(QSize(80,80))
        self.MenButton3.setToolTip("Teen Men Ideal Workout")
        self.MenButton3.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.MenButton3.move(650,450)
        self.MenButton3.resize(120,120)
        self.MenButton3.clicked.connect(self.ManWork)3

        self.WomenButton3 = QPushButton('Teen Women',self)
        self.WomenButton3.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.WomenButton3.move(690,570)
        self.WomenButton3.setIcon(QIcon('man.png'))
        self.WomenButton3.setIconSize(QSize(80,80))
        self.WomenButton3.setToolTip("Teen Women Ideal Workout")
        self.WomenButton3.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.WomenButton3.resize(120,120)
        self.WomenButton3.clicked.connect(self.WomanWork3)

    def ManWork(self):
        Workout_console.hide(self)
        self.man = sman()
        self.man.show()

    def WomanWork(self):
        Workout_console.hide(self)
        self.wman = swman()
        self.wman.show()
    
    def ManWork2(self):
        Workout_console.hide(self)
        self.man = aman()
        self.man.show()

    def WomanWork2(self):
        Workout_console.hide(self)
        self.wman = awman()
        self.wman.show()
    
    def ManWork3(self):
        Workout_console.hide(self)
        self.man = tman()
        self.man.show()

    def WomanWork3(self):
        Workout_console.hide(self)
        self.wman = twman()
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
        image1 = image.scaled(QSize(500,100))
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
        image1 = image.scaled(QSize(500,100))
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

class aman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Senior Woman Ideal Workout")
        self.setWindowIcon(QIcon('woman.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(500,100))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Adult Man Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Balance and flexibility focus", self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Cardio-heavy", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3. Traditional lifts", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. Weight-management workouts", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Jogging", self)
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
        self.open = adult()
        self.open.show()

class awman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Adult Woman Ideal Workout")
        self.setWindowIcon(QIcon('woman.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(500,100))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Adult Woman Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Burpees", self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Squats", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3.Plank", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. Push Dumbbells", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Walk", self)
        self.workout5.setFont(QFont('Times', 20, QFont.Bold))
        self.workout5.setStyleSheet('QLabel {color:#dedede}')
        self.workout5.move(380, 200)
        self.workout5.resize(120, 30)

        self.pushButton = QPushButton('Go Back', self)
        self.pushButton.setStyleSheet("""text-decoration: underline;color: white;font-family: Arial; font-weight: bold""")
        self.pushButton.move(30,750)
        self.pushButton.setIcon(QIcon('woman.png'))
        self.pushButton.setIconSize(QSize(80,80))
        self.pushButton.setToolTip("Go Back to Workout Ideas age gap selection")
        self.pushButton.setStyleSheet("background-color: #FFDF00; border-radius:40px; border-style: outset ; border-width: 0.8px;border-radius: 40px;")
        self.pushButton.resize(120,120)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        sman.hide(self)
        self.open = adult()
        self.open.show()

class tman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Teen Woman Ideal Workout")
        self.setWindowIcon(QIcon('woman.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(500,100))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Teen Man Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Bench press , self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Squats", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3. Deadlift", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. Shoulder press", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Shadow Boxing or any sports", self)
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
        self.open = teen()
        self.open.show()

class twman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(80, 100, 1000, 800)
        self.setWindowTitle("Teen Woman Ideal Workout")
        self.setWindowIcon(QIcon('woman.png'))

        image = QImage('bg0.jpg')
        image1 = image.scaled(QSize(500,100))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image1))
        self.setPalette(palette)

        self.labeling = QLabel("<h4> 5 Teen Woman Workout Ideas <h4>", self)
        self.labeling.setFont(QFont('Times', 20, QFont.Bold))
        self.labeling.setStyleSheet('QLabel {color:#dedede;}')
        self.labeling.move(380, 20)
        self.labeling.resize(120, 30)

        self.workout1 = QLabel("<h4> 1. Squats", self)
        self.workout1.setFont(QFont('Times', 20, QFont.Bold))
        self.workout1.setStyleSheet('QLabel {color:#dedede}')
        self.workout1.move(380, 60)
        self.workout1.resize(120, 30)
        
        self.workout2 = QLabel("<h4> 2. Bicycle Crunches", self)
        self.workout2.setFont(QFont('Times', 20, QFont.Bold))
        self.workout2.setStyleSheet('QLabel {color:#dedede}')
        self.workout2.move(380, 100)
        self.workout2.resize(120, 30)

        self.workout3 = QLabel("<h4> 3.  Lying Leg Lifts", self)
        self.workout3.setFont(QFont('Times', 20, QFont.Bold))
        self.workout3.setStyleSheet('QLabel {color:#dedede}')
        self.labeling.move(380, 120)
        self.labeling.resize(120, 30)

        self.workout4 = QLabel("<h4> 4. V-Sit", self)
        self.workout4.setFont(QFont('Times', 20, QFont.Bold))
        self.workout4.setStyleSheet('QLabel {color:#dedede}')
        self.workout4.move(380, 160)
        self.workout4.resize(120, 30)

        self.workout5 = QLabel("<h4> 5. Bend And Kick Back", self)
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
        self.open = teen()
        self.open.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Intro()
    sys.exit(app.exec_())
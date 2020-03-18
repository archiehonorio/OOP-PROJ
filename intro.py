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
        self.button.setGeometry(50, 600, 300, 50)
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
                print("hehe")
            elif ageStruc['age'] <= ageGap3:
                print("asdada")
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


        self.computation = QPushButton
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Intro()
    sys.exit(app.exec_())
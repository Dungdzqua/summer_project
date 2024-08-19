from abstract import UIN
from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel , QFrame , QSplitter , QVBoxLayout , QWidget , QScrollArea
from PyQt5.QtCore import Qt , QTimer
from datetime import datetime
from time import sleep
import readcsv as csv 
import style

class MathGUI(UIN):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("f2")
        spillter = QSplitter(Qt.Horizontal)

        #frame1
        frameCot = QFrame()
        frameCot.setGeometry(0,0,150,100)
        frameCot.setStyleSheet("background-color:rgb(175,200,173)")
        spillter.addWidget(frameCot)

        #frame chinh
        frameMain = QFrame()
        frameMain.setStyleSheet("background-color:rgb(136,171,142)")
        spillter.addWidget(frameMain)

        Cbox = QVBoxLayout()
        Cbox.setContentsMargins(0,0,0,0)
        Cbox.addWidget(spillter)

        widget = QWidget()
        widget.setLayout(Cbox)
        self.setCentralWidget(widget)
        #finish
        # self._finishbutton=QPushButton("Finish",frameMain)
        # self._finishbutton.clicked.connect(finishbutton,self)

        #timer
        self._startButton=QPushButton("START",frameCot)
        self._startButton.setGeometry(20,150,350,120)
        self._startButton.clicked.connect(self.countdown)
        self._startButton.setStyleSheet(style.startBuuonnn)
        self.time = 10

        self.timerprint=QLabel(frameCot)
        self.timerprint.setGeometry(80,20,240,100)
        self.timerprint.setText(datetime.fromtimestamp(self.time).strftime("%M:%S"))
        self.timerprint.setStyleSheet(style.timerstyle)
        self.timerprint.setAlignment(Qt.AlignCenter)

        # list câu hỏi
        self.scroll_widget= QWidget()
        self.scroll_layout= QVBoxLayout(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area = QScrollArea(frameCot)
        self.scroll_area.setGeometry(0,420,400,430)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.show()


        self._questiontxt=QLabel(frameMain)
        self._questiontxt.setText('chon cau hoi')
        self._questiontxt.setGeometry(70,65,750,200)
        self._questiontxt.setStyleSheet(style.wellcomTxt)

        self.chinhstrA='neige'
        self.chinhstrB='neige'
        self.chinhstrC='neige'
        self.chinhstrD='neige'

        self.questionInd=None
        self.currChoice=None

        self.cAButton = QPushButton(f'{self.chinhstrA}',frameMain)
        self.cAButton.setGeometry(50,400,400,170)
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cAButton.clicked.connect(self.selcA)

        self.cBButton = QPushButton(f'{self.chinhstrB}',frameMain)
        self.cBButton.setGeometry(600,400,400,170)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.clicked.connect(self.selcB)

        self.cCButton = QPushButton(f'{self.chinhstrC}',frameMain)
        self.cCButton.setGeometry(50,620,400,170)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.clicked.connect(self.selcC)

        self.cDButton = QPushButton(f'{self.chinhstrD}',frameMain)
        self.cDButton.setGeometry(600,620,400,170)
        self.cDButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.clicked.connect(self.selcD)
        #create question index
        for txt in range(0,len(csv.csvList)):
            self.i=f'{txt+1}'
            self._button = QPushButton(self.i,self.scroll_area)
            self.scroll_layout.addWidget(self._button)
            self._button.setStyleSheet(style.listStyle)
            self._button.show()
            self._button.clicked.connect(lambda ch, idx=txt: self.showChoice(idx))
        #create user answer list
        self.userans=[]
        for x in range(0,len(csv.csvList)):
            self.userans.append(None)
        
        #finish button
        self._finishButton = QPushButton("FINISH",frameCot)
        self._finishButton.setGeometry(20,280,350,120)
        self._finishButton.setStyleSheet(style.finishButton)



    # def finishbutton(self):
    #     self.nextUI=MainUI()
    #     self.nextUI.show()
    #     self.hide()


    def selcA(self):
        self.cAButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButton)
        self.userans[self.questionInd]='A'
        print(f'a:{self.questionInd}')


    def selcB(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButton)
        self.userans[self.questionInd]='B'
        print(f'b:{self.questionInd}')

    def selcC(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cDButton.setStyleSheet(style.ChoiceButton)
        self.userans[self.questionInd]='C'
        print(f'c:{self.questionInd}')


    def selcD(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButtonEffect)
        self.userans[self.questionInd]='D'
        print(f'd:{self.questionInd}')


    def showChoice(self,ind):
        choi=csv.csvList
        self._questiontxt.setText(str(choi[ind][0]))

        self.questionInd=ind

        textButtonA=str(choi[ind][1])
        textButtonB=str(choi[ind][2])
        textButtonC=str(choi[ind][3])
        textButtonD=str(choi[ind][4])

        self.cAButton.setText(textButtonA)
        self.cBButton.setText(textButtonB)
        self.cCButton.setText(textButtonC)
        self.cDButton.setText(textButtonD)

        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButton)
        print(self.userans)
        # print('index is'+str(ind))
        # print(self.choi[ind])
        # print(f"A:{self.chinhstrA}")
        # print(f"B:{self.chinhstrB}")
        # print(f"C:{self.chinhstrC}")
        # print(f"D:{self.chinhstrD}")

    def countdown(self): 
        self.timer= QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self._startButton.setStyleSheet(style.startButtonAc)
    
    def updateTime(self):
        if self.time > 0 :
            self.time -=1
            self.currTime = datetime.fromtimestamp(self.time).strftime("%M:%S")
            self.timerprint.setText(f'{self.currTime}')
        else:
            self.timer.stop()
            
  
  
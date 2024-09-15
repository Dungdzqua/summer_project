from abstract import UIN
from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel , QFrame , QSplitter , QVBoxLayout , QWidget , QScrollArea
from PyQt5.QtCore import Qt , QTimer
from datetime import datetime
from time import sleep
from finalscreen import ScoreGUI
import readcsv as csv 
import style
class MathGUI(UIN):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("f2")
        spillter = QSplitter(Qt.Horizontal)

        #frame1
        frameCot = QFrame()
        frameCot.setGeometry(0,0,245,100)
        frameCot.setStyleSheet("background-color:rgb(175,200,173)")
        spillter.addWidget(frameCot)

        #frame chinh
        frameMain = QFrame()
        frameMain.setStyleSheet("background-color:rgb(136, 171, 142)")
        spillter.addWidget(frameMain)

        Cbox = QVBoxLayout()
        Cbox.setContentsMargins(0,0,0,0)
        Cbox.addWidget(spillter)

        widget = QWidget()
        widget.setLayout(Cbox)
        self.setCentralWidget(widget)

        #timer
        self._startButton=QPushButton("START",frameCot)
        self._startButton.setGeometry(20,150,350,120)
        self._startButton.clicked.connect(self.countdown)
        self._startButton.setStyleSheet(style.startBuuonnn)
        self.time = 300
        self.timerc=False
    
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
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")
        self.scroll_area.setEnabled(False)
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
        print(self.userans)
        #finish button
        self._finishButton = QPushButton("FINISH",frameCot)
        self._finishButton.setGeometry(20,280,350,120)
        self._finishButton.setStyleSheet(style.finishButton)
        self._finishButton.clicked.connect(self.finishbutton)

    def EffectA(self):
        self.cAButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButton)
    def selcA(self):
        self.EffectA()
        self.userans[self.questionInd]='A'
        print(f'ind: {self.questionInd}')
        print(f'a:{self.questionInd}')

    def EffectB(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButton)
    def selcB(self):
        self.EffectB()
        self.userans[self.questionInd]='B'
        print(f'ind: {self.questionInd}')
        print(f'b:{self.questionInd}')

    def EffectC(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButtonEffect)
        self.cDButton.setStyleSheet(style.ChoiceButton)

    def selcC(self):
        self.EffectC()
        print(f'c:{self.questionInd}')
        self.userans[self.questionInd]='C'
        print(f'ind: {self.questionInd}')

    def EffectD(self):
        self.cAButton.setStyleSheet(style.ChoiceButton)
        self.cBButton.setStyleSheet(style.ChoiceButton)
        self.cCButton.setStyleSheet(style.ChoiceButton)
        self.cDButton.setStyleSheet(style.ChoiceButtonEffect)
    def selcD(self):
        self.EffectD()
        self.userans[self.questionInd]='D'
        print(f'ind: {self.questionInd}')
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

        if self.userans[self.questionInd]=='A':
            self.EffectA()
        elif self.userans[self.questionInd]=='B':
            self.EffectB()
        elif self.userans[self.questionInd]=='C':
            self.EffectC()
        elif self.userans[self.questionInd]=='D':
            self.EffectD()
    def countdown(self): 
        self.timer= QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self._startButton.setStyleSheet(style.startButtonAc)
        self._startButton.setEnabled(False)
        self.scroll_area.setEnabled(True)

    
    def updateTime(self):
        if self.time > 0 :
            self.timerc=True
            self.time -=1
            self.currTime = datetime.fromtimestamp(self.time).strftime("%M:%S")
            self.timerprint.setText(f'{self.currTime}')
        else:
            self.timer.stop()
            self.finishbutton()
    def finishbutton(self):
        sendTime=self.time
        print(sendTime)
        print(self.userans)
        if self.timerc:
            self.timer.stop()
        self.nextUI=ScoreGUI(sendTime,self.userans)
        self.nextUI.show()
        self.hide()
            
  
  
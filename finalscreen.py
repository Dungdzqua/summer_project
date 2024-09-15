from abstract import UIN
from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel , QFrame , QSplitter , QVBoxLayout , QWidget , QScrollArea
from PyQt5.QtCore import Qt , QTimer
from datetime import datetime
from time import sleep
import readcsv as rcsv
import style
import MathUI as mtui
class ScoreGUI(UIN):
    def __init__(self,timert,userans):
        super().__init__()
        self.setWindowTitle("final screen")
        spillter = QSplitter(Qt.Horizontal)
        #background
        self.setStyleSheet("background-color:rgb(136, 171, 142)")

        # Create main frameMain
        frameMain = QFrame(self)
        frameMain.setStyleSheet("background-color: #AFC8AD; padding: 20px; border-radius: 10px;")
        frameMain.setGeometry(50,50,1340,800)
    
        # Create the layout
        layout = QVBoxLayout()

        # Set layout for the frameMain
        frameMain.setLayout(layout)

        # Create the main layout for the window
        main_layout = QVBoxLayout()
        main_layout.addWidget(frameMain)

        # Set the layout for the main window
        self.setLayout(main_layout)

        #check ans
        print(userans)
        print(rcsv.ListAnswer)
        self._correctans=0
        for x in range(0,10):
            a=userans[x]
            b=rcsv.ListAnswer[x]
            print('---Ind---')
            print(x)
            if userans[x] == rcsv.ListAnswer[x]:
                self._correctans+=1
                print(f'{a} == {b}')
                print(f'yes: {x+1}')
            else:
                print('unco')
                print(f'{a}!={b}')
        

        # label for answer
            # so cau dung
        self._Labelcorrectans=QLabel(frameMain)
        self._Labelcorrectans.setText(f'số câu đúng: {self._correctans}')
        self._Labelcorrectans.setGeometry(100,250,350,100)
        self._Labelcorrectans.setStyleSheet(style.answerCheckTxt)

            #so cau sai
        self._unccans=10-self._correctans
        self._Labelunccans=QLabel(frameMain)
        self._Labelunccans.setText(f'số câu sai: {self._unccans}')
        self._Labelunccans.setGeometry(100,250,350,100)
        self._Labelunccans.setStyleSheet(style.answerCheckTxt)

            #timer
        self._Timercalc=300-timert
        self._Timerp=datetime.fromtimestamp(self._Timercalc).strftime("%M:%S")
        self._LabelTimer=QLabel(frameMain)
        self._LabelTimer.setGeometry(100,300,700,100)
        self._LabelTimer.setText(f'Thời gian làm: {self._Timerp}')
        self._LabelTimer.setStyleSheet(style.answerCheckTxt)

            #tong ket txt
        self._LabelTongketstr=QLabel(frameMain)
        self._LabelTongketstr.setText("TỔNG KẾT")
        self._LabelTongketstr.setGeometry(350,10,590,200)
        self._LabelTongketstr.setAlignment(Qt.AlignCenter)
        self._LabelTongketstr.setStyleSheet(style.FinalScreenTxt)

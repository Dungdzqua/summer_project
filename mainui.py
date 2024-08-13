from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel , QFrame , QSplitter , QVBoxLayout , QWidget
from PyQt5.QtCore import Qt 
from MathUI import MathGUI
from abstract import UIN
from time import sleep
import style
class MainUI(UIN):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("f1")
        spillter = QSplitter(Qt.Horizontal)


        #frame1
        frameCot = QFrame()
        frameCot.setGeometry(0,0,200,400)
        frameCot.setStyleSheet("background-color:rgb(175,200,173)")
        spillter.addWidget(frameCot)

        #frame chinh
        frameMain = QFrame()
        # frameMain.setGeometry(0,0,400,309)
        frameMain.setStyleSheet("background-color:rgb(136,171,142)")
        spillter.addWidget(frameMain)

        Cbox = QVBoxLayout()
        Cbox.setContentsMargins(0,0,0,0)
        Cbox.addWidget(spillter)

        widget = QWidget()
        widget.setLayout(Cbox)

        # chon mon hoc
        self._selctxt=QLabel(frameMain)
        self._selctxt.setText("CHỌN MÔN HỌC")
        self._selctxt.setGeometry(100,50,900,200)
        self._selctxt.setStyleSheet(style.wellcomTxt)
        self._selctxt.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(widget)

        self._Math=QPushButton("Math",frameMain)
        self._Math.setGeometry(100,300,300,150) 
        self._Math.clicked.connect(self.MathUI)
        self._Math.setStyleSheet(style.button_f1)


        
        self._Che=QPushButton("che",frameMain)
        self._Che.setGeometry(700,300,300,150) 
        self._Che.clicked.connect(self.MathUI)
        self._Che.setStyleSheet(style.button_f1)


        self._vatLon=QPushButton("vat lon",frameMain)
        self._vatLon.setGeometry(100,550,300,150) 
        self._vatLon.clicked.connect(self.MathUI)
        self._vatLon.setStyleSheet(style.button_f1)


        self._sinh=QPushButton("sinh",frameMain)
        self._sinh.setGeometry(700,550,300,150) 
        self._sinh.clicked.connect(self.MathUI)
        self._sinh.setStyleSheet(style.button_f1)
        

        
    def MathUI(self):
        self._Math.setStyleSheet(style.buttonEffect_f1)
        sleep(0.2)
        self._Math.setStyleSheet(style.buttonEffect_f1)

        self.nextUI=MathGUI()
        self.nextUI.show()
        self.hide()



from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel
import time 


class UIN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x=0
        self.y=24
        self.width=1439
        self.height=900
        self.setGeometry(self.x,self.y,self.width,self.height)
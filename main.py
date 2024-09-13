import sys

from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import QSize
from PyQt5 import uic
from PyQt5.QtGui import QColor
from abc import ABC,abstractmethod
import time 

#import UI
from mainui import MainUI
from MathUI import MathGUI
# from finalscreen import ScoreGUI
app= QApplication([])

GUI=MainUI()
GUI.show()
app.exec_()





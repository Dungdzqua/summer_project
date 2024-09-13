from abstract import UIN
from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow, QLabel , QFrame , QSplitter , QVBoxLayout , QWidget , QScrollArea
from PyQt5.QtCore import Qt , QTimer
from datetime import datetime
from time import sleep
import readcsv as csv 
import style

class ScoreGUI(UIN):
    def __init__(self):
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


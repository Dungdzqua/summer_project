import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button Click Example')
        self.setGeometry(100, 100, 400, 600)
        
        self.layout = QVBoxLayout()

        # Danh sách dữ liệu
        self.data_list = [['1.A', '1.B', '1.C', '1.D'], 
                          ['2.A', '2.B', '2.C', '2.D'], 
                          ['3.A', '3.B', '3.C', '3.D'], 
                          ['4.A', '4.B', '4.C', '4.D'], 
                          ['5.A', '5.B', '5.C', '5.D'], 
                          ['6.A', '6.B', '6.C', '6.D'], 
                          ['7.A', '7.B', '7.C', '7.D'], 
                          ['8.A', '8.B', '8.C', '8.D'], 
                          ['9.A', '9.B', '9.C', '9.D'], 
                          ['10.A', '10.B', '10.C', '10.D'], 
                          ['11.A', '11.B', '11.C', '11.D'], 
                          ['12.A', '12.B', '12.C', '12.D'], 
                          ['13.A', '13.B', '13.C', '13.D'], 
                          ['14.A', '14.B', '14.C', '14.D'], 
                          ['15.A', '15.B', '15.C', '15.D'], 
                          ['16.A', '16.B', '16.C', '16.D'], 
                          ['17.A', '17.B', '17.C', '17.D'], 
                          ['18.A', '18.B', '18.C', '18.D'], 
                          ['19.A', '19.B', '19.C', '19.D'], 
                          ['20.A', '20.B', '20.C', '20.D']]

        # Tạo một danh sách các nút để lưu các nút đã tạo
        self.buttons = []

        # Tạo các nút từ danh sách dữ liệu sử dụng for x in range
        for i in range(len(self.data_list)):
            button = QPushButton(f'Button {i+1}', self)
            button.clicked.connect(lambda ch, idx=i: self.on_click(idx, button))
            self.layout.addWidget(button)
            self.buttons.append(button)
        
        # QLabel để hiển thị giá trị
        self.label = QLabel('Click a button to see its value', self)
        self.layout.addWidget(self.label)
        
        self.setLayout(self.layout)
    
    def on_click(self, index, button):
        # Cập nhật QLabel với giá trị của phần tử tại index từ danh sách dữ liệu
        self.label.setText(f'Value: {self.data_list[index]}')
        # Cập nhật văn bản của nút đã được nhấn
        new_text = f'{index+1}.{chr(65 + (index % 4))}'  # Bạn có thể thay đổi logic cập nhật văn bản tùy ý
        button.setText(new_text)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

# 한국환경공단의 미세먼지 정보를 테이블에 출력하고 그래프 표시
# 500 x 650 크기 윈도우 생성
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.setLayout(layout)
        self.setWindowTitle('My Window')        
        self.setGeometry(300, 300, 500, 650)    
        self.show()                             
        

if __name__ == '__main__':      
    app = QApplication(sys.argv)
    ex = MyApp()                
    sys.exit(app.exec_())      
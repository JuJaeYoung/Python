import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):           # 클래스 정의

    def __init__(self):
        
        super().__init__()      # 부모클래스 생성자 호출(가장 위쪽 코딩)
        self.initUI()

        
    def btnClicked(self):       # 이벤트 핸들러 함수 작성
        sender = self.sender()  # 이벤트 소스를 저장(버튼, 체크박스 등)
        self.label1.setText(sender.text() + '이 눌렀습니다')
     
    
    def btn3Clicked(self):
        QMessageBox.warning(self, '경고', '에러')
        
        
    def initUI(self):           # 윈도우 환경 구성
        
        self.btn1 = QPushButton('버튼1')
        self.btn2 = QPushButton('버튼2')
        self.btn1.clicked.connect(self.btnClicked)
        self.btn2.clicked.connect(self.btnClicked)
        
        self.btn3 = QPushButton('버튼3')
        self.btn4 = QPushButton('버튼4')
        self.btn3.clicked.connect(self.btn3Clicked)
        self.btn4.clicked.connect(self.btnClicked)
        
        self.btn5 = QPushButton('버튼5')
        self.btn6 = QPushButton('버튼6')
        self.btn5.clicked.connect(self.btnClicked)
        self.btn6.clicked.connect(self.btnClicked)
        
        self.label1 = QLabel('누가 시그널을 보냈을까?')
    
        layout = QHBoxLayout()                  # 수평상자 배치관리자(최상위)
        
        layoutLeft = QVBoxLayout()              # 수직상자 배치관리자        
        layoutTop = QHBoxLayout()               # 위쪽 배치관리자
        layoutBottom = QVBoxLayout()            # 아래쪽 배치관리자
        
        layoutRight = QVBoxLayout()             # 오른쪽 배치관리자
        
        layoutTop.addWidget(self.btn1)
        layoutTop.addWidget(self.btn2)
        
        layoutBottom.addWidget(self.btn3)
        layoutBottom.addWidget(self.btn4)
        layoutBottom.addWidget(self.label1)
        
        layoutRight.addWidget(self.btn5)
        layoutRight.addWidget(self.btn6)
        
        layoutLeft.addLayout(layoutTop)
        layoutLeft.addLayout(layoutBottom)
        
        layout.addLayout(layoutLeft)
        layout.addLayout(layoutRight)
        
        
        self.setLayout(layout)
        self.setWindowTitle('My Window')        # 윈도우 타이틀
        self.setGeometry(10, 30, 800, 600)      # 좌상단 좌표, 너비, 높이
        self.show()                             # 윈도우 보이기
 
        
if __name__ == '__main__':      # 진입점 판단(운영체제에서 프로그램 호출)
    app = QApplication(sys.argv)
    ex = MyApp()                # 클래스 객체 생성
    sys.exit(app.exec_())       # 프로그램 실행상태 유지(윈도우 실행)
    
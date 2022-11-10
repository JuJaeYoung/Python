# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ddareung_6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os

os.chdir(os.getcwd())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 957)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1089, 896))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1060, 870))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dataHead = QtWidgets.QTextEdit(self.frame)
        self.dataHead.setGeometry(QtCore.QRect(10, 30, 1031, 101))
        self.dataHead.setObjectName("dataHead")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.dataPre = QtWidgets.QTextBrowser(self.frame)
        self.dataPre.setGeometry(QtCore.QRect(40, 170, 261, 470))
        self.dataPre.setObjectName("dataPre")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(350, 150, 56, 12))
        self.label_3.setObjectName("label_3")
        self.imgLabel = QtWidgets.QLabel(self.frame)
        self.imgLabel.setGeometry(QtCore.QRect(350, 170, 651, 470))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.trainPath = QtWidgets.QTextBrowser(self.frame)
        self.trainPath.setGeometry(QtCore.QRect(10, 710, 630, 31))
        self.trainPath.setObjectName("trainPath")
        self.testPath = QtWidgets.QTextBrowser(self.frame)
        self.testPath.setGeometry(QtCore.QRect(10, 770, 630, 31))
        self.testPath.setObjectName("testPath")
        self.trainBtn = QtWidgets.QPushButton(self.frame)
        self.trainBtn.setGeometry(QtCore.QRect(660, 710, 75, 30))
        self.trainBtn.setObjectName("trainBtn")
        self.testBtn = QtWidgets.QPushButton(self.frame)
        self.testBtn.setGeometry(QtCore.QRect(660, 770, 75, 30))
        self.testBtn.setObjectName("testBtn")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 750, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 810, 111, 16))
        self.label_6.setObjectName("label_6")
        self.learnBtn = QtWidgets.QPushButton(self.frame)
        self.learnBtn.setGeometry(QtCore.QRect(950, 720, 111, 141))
        self.learnBtn.setObjectName("learnBtn")
        self.hour = QtWidgets.QCheckBox(self.frame)
        self.hour.setGeometry(QtCore.QRect(760, 720, 81, 16))
        self.hour.setObjectName("hour")
        self.temperature = QtWidgets.QCheckBox(self.frame)
        self.temperature.setGeometry(QtCore.QRect(760, 750, 91, 16))
        self.temperature.setObjectName("temperature")
        self.precipitation = QtWidgets.QCheckBox(self.frame)
        self.precipitation.setGeometry(QtCore.QRect(760, 780, 91, 16))
        self.precipitation.setObjectName("precipitation")
        self.windspeed = QtWidgets.QCheckBox(self.frame)
        self.windspeed.setGeometry(QtCore.QRect(760, 810, 81, 16))
        self.windspeed.setObjectName("windspeed")
        self.humidity = QtWidgets.QCheckBox(self.frame)
        self.humidity.setGeometry(QtCore.QRect(760, 840, 81, 16))
        self.humidity.setObjectName("humidity")
        self.visibility = QtWidgets.QCheckBox(self.frame)
        self.visibility.setGeometry(QtCore.QRect(860, 720, 81, 16))
        self.visibility.setObjectName("visibility")
        self.pm2_5 = QtWidgets.QCheckBox(self.frame)
        self.pm2_5.setGeometry(QtCore.QRect(860, 810, 81, 16))
        self.pm2_5.setObjectName("pm2_5")
        self.pm10 = QtWidgets.QCheckBox(self.frame)
        self.pm10.setGeometry(QtCore.QRect(860, 780, 81, 16))
        self.pm10.setObjectName("pm10")
        self.ozoen = QtWidgets.QCheckBox(self.frame)
        self.ozoen.setGeometry(QtCore.QRect(860, 750, 81, 16))
        self.ozoen.setObjectName("ozoen")
        self.All_ = QtWidgets.QCheckBox(self.frame)
        self.All_.setGeometry(QtCore.QRect(860, 840, 81, 16))
        self.All_.setObjectName("All_")
        self.subPath = QtWidgets.QTextBrowser(self.frame)
        self.subPath.setGeometry(QtCore.QRect(10, 830, 630, 31))
        self.subPath.setObjectName("subPath")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 690, 71, 16))
        self.label_7.setObjectName("label_7")
        self.subBtn = QtWidgets.QPushButton(self.frame)
        self.subBtn.setGeometry(QtCore.QRect(660, 830, 75, 30))
        self.subBtn.setObjectName("subBtn")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def trPath(self) :
        a = QtWidgets.QFileDialog.getOpenFileName()
        f = pd.read_csv(a[0])
        self.trainPath.setText(a[0])
        self.dataHead.setText(str(f))

    def tsPath(self) :
        a = QtWidgets.QFileDialog.getOpenFileName()
        f = pd.read_csv(a[0])
        self.testPath.setText(a[0])
        self.dataHead.setText(str(f))

    def sbPath(self) :
        a = QtWidgets.QFileDialog.getOpenFileName()
        f = pd.read_csv(a[0])
        self.subPath.setText(a[0])
        self.dataHead.setText(str(f))    

    def learn(self) :
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        # import warnings
        import tensorflow as tf

        

        from sklearn.linear_model import LinearRegression      # 선형회귀
        from sklearn.ensemble import RandomForestRegressor     # 랜덤포레스트
        from xgboost import XGBRegressor

        if self.All_.isChecked() == False:
            while True :
                if self.hour.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.temperature.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.precipitation.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.windspeed.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.humidity.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.visibility.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.pm2_5.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.pm10.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.ozoen.isChecked() == False :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                    

                break

        # 데이터 불러오기
        a = self.trainPath.toPlainText()
        b = self.testPath.toPlainText()
        c = self.subPath.toPlainText()
        train = pd.read_csv(a)
        test = pd.read_csv(b)
        submission = pd.read_csv(c)

        x = []
        
        if self.hour.isChecked() == True :
            x.append("hour")
            
        if self.temperature.isChecked() == True :
            x.append("temperature")
            
        if self.precipitation.isChecked() == True :
            x.append("precipitation")
            
        if self.windspeed.isChecked() == True :
            x.append("windspeed")
            
        if self.humidity.isChecked() == True :
            x.append("humidity")
            
        if self.visibility.isChecked() == True :
            x.append("visibility")
            
        if self.pm2_5.isChecked() == True :
            x.append("pm2_5")
            
        if self.pm10.isChecked() == True :
            x.append("pm10")
            
        if self.ozoen.isChecked() == True :
            x.append("ozoen")
            
        if self.All_.isChecked() == True :
            while True : 
                if self.hour.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.temperature.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.precipitation.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.windspeed.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.humidity.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.visibility.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.pm2_5.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.pm10.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break
                if self.ozoen.isChecked() == True :
                    self.dataPre.setText("설정을 다시하세요")
                    break

                break
            
            x.extend(["hour","temperature","precipitation","windspeed","humidity","visibility","pm2_5","pm10","ozoen"])

            
            
        # 데이터 불러오기
        a = self.trainPath.toPlainText()
        b = self.testPath.toPlainText()
        c = self.subPath.toPlainText()
        train = pd.read_csv(a)
        test = pd.read_csv(b)
        submission = pd.read_csv(c)
        

        # train 데이터셋 결측치 처리
        train['hour_bef_precipitation'].fillna('0', inplace=True)
        train.fillna(method = 'ffill', inplace=True)
        
        # test 데이터셋 결측치 처리
        test['hour_bef_precipitation'].fillna('0', inplace=True)
        test.fillna(method = 'ffill', inplace=True)
        
        # 변수명 수정
        train.rename(columns={'hour_bef_temperature':'temperature', 'hour_bef_precipitation':'precipitation', 
                      'hour_bef_windspeed':'windspeed', 'hour_bef_humidity':'humidity', 
                      'hour_bef_visibility':'visibility', 'hour_bef_ozone':'ozoen', 
                      'hour_bef_pm10':'pm10', 'hour_bef_pm2.5':'pm2_5'}, inplace=True)
        
        test.rename(columns={'hour_bef_temperature':'temperature', 'hour_bef_precipitation':'precipitation', 
                      'hour_bef_windspeed':'windspeed', 'hour_bef_humidity':'humidity', 
                      'hour_bef_visibility':'visibility', 'hour_bef_ozone':'ozoen', 
                      'hour_bef_pm10':'pm10', 'hour_bef_pm2.5':'pm2_5'}, inplace=True)
        

        # 변수 정의
        x_train = train[x]
        
        y_train = train['count']
        x_test = test[x]

        # ============== LinearRegressor =============
        # 모델 생성
        model_LR = LinearRegression()

        # 학습
        model_LR.fit(x_train, y_train)

        # 예측값
        y_pred_LR = model_LR.predict(x_test)
        # y2 = str(y_pred_LR)
        # self.dataPre.setText(y2)

        # ================ RandomForestRegressor ====================
        # 모델 생성
        model_RF100 = RandomForestRegressor(n_estimators=100, random_state=0)

        # 모델 학습
        model_RF100.fit(x_train, y_train)

        # 예측값
        y_pred_RF100 = model_RF100.predict(x_test)

        # =============== XGBRegressor =================
        # 모델 생성
        model_XGB = XGBRegressor(max_depth = 4, n_estimators = 500)

        # 모델 학습
        model_XGB.fit(x_train.astype(np.float32), y_train.astype(np.float32))

        # 예측값
        y_pred_XGB = model_XGB.predict(x_test.astype(np.float32))

        # 3가지 모델의 평균을 예측값으로
        submission['count'] = (y_pred_LR + y_pred_RF100 + y_pred_XGB) / 3
        submission['count_LR'] = y_pred_LR
        submission['count_RF100'] = y_pred_RF100
        submission['count_XGB'] = y_pred_XGB

        # 결과 값 초기화
        self.dataPre.setText("")
        # 결과 저장을 위한 데이터
        sub = submission[['id','count']]

        sub.to_csv("final_result.csv", index=False)
        
        f = open("final_result.csv")
        lines = f.readlines()
        
        for line in lines[1:]:
            a, b = line.split(',')
            index = b.find('.')
                       
            self.dataPre.append('id : ' +  a)
            self.dataPre.append('count : ' + b[:index])
            self.dataPre.append('\t')
            
        f.close()

        # 히트맵 그리기 위한 데이터
        result = submission.drop(['id'], axis=1)

        plt.figure(figsize=(10,10))
        sns.heatmap(result.corr(), annot=True, fmt=".5f", linewidths=.5, 
                    square=True, cmap='Blues_r', vmin=0.7, vmax=1)
        plt.gcf().set_size_inches(10, 10)
        plt.title("Heatmap of Models")

        plt.savefig("model_heatmap.png", dpi=70, bbox_inches='tight')

        self.imgLabel.setPixmap(QtGui.QPixmap("model_heatmap.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Data Head"))
        self.label_2.setText(_translate("MainWindow", "Predict"))
        self.label_3.setText(_translate("MainWindow", "Graph"))
        self.trainBtn.setText(_translate("MainWindow", "Train Open"))
        self.testBtn.setText(_translate("MainWindow", "Test Open"))
        self.label_5.setText(_translate("MainWindow", "Test Path"))
        self.label_6.setText(_translate("MainWindow", "Submission Path"))
        self.learnBtn.setText(_translate("MainWindow", "Learning"))
        self.hour.setText(_translate("MainWindow", "hour"))
        self.temperature.setText(_translate("MainWindow", "temperature"))
        self.precipitation.setText(_translate("MainWindow", "precipitation"))
        self.windspeed.setText(_translate("MainWindow", "windspeed"))
        self.humidity.setText(_translate("MainWindow", "humidity"))
        self.visibility.setText(_translate("MainWindow", "visibility"))
        self.pm2_5.setText(_translate("MainWindow", "pm2.5"))
        self.pm10.setText(_translate("MainWindow", "pm10"))
        self.ozoen.setText(_translate("MainWindow", "ozone"))
        self.All_.setText(_translate("MainWindow", "All"))
        self.label_7.setText(_translate("MainWindow", "Open Path"))
        self.subBtn.setText(_translate("MainWindow", "Sub Open"))
        self.trainBtn.clicked.connect(self.trPath)
        self.testBtn.clicked.connect(self.tsPath)
        self.subBtn.clicked.connect(self.sbPath)
        self.learnBtn.clicked.connect(self.learn)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


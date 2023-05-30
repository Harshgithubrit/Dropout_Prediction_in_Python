from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pickle
from Preprocessing import preprocess_features
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics


class Ui_Prediction(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "*.csv")
        self.lineEdit.setText(fileName)
    def prediction(self):
        try:
            filename = self.lineEdit.text()
            Alg = self.comboBox.currentText()
            if Alg == "-------------Select --------------" :
                self.alertmsg("Error", "Please select the Algorithm")
            elif filename == "" or filename=="null":
                self.alertmsg("Error","Please select the File")
            elif Alg=="Decision Tree Classifier":
                testing_data = self.lineEdit.text()
                student_data = pd.read_csv(testing_data)
                feature_cols = list(student_data.columns)
                x_test = student_data[feature_cols]
                x_test = preprocess_features(x_test)
                model = open('../DropoutPrediction/model/DT.model', 'rb')
                clf_dt = pickle.load(model)
                predicted = clf_dt.predict(x_test)
                result = predicted[0]
                self.res.setText(result)
            elif Alg=="Gaussian Naive Bayes" :
                testing_data = self.lineEdit.text()
                student_data = pd.read_csv(testing_data)
                feature_cols = list(student_data.columns)
                x_test = student_data[feature_cols]
                x_test = preprocess_features(x_test)
                model = open('../DropoutPrediction/model/NB.model', 'rb')
                clf_dt = pickle.load(model)
                predicted = clf_dt.predict(x_test)
                result = predicted[0]
                self.res.setText(result)
            else:
                self.alertmsg("Failed","Fill all The Details")

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print("LINE NO: ", tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setStyleSheet("QDialog{background-image: url(../DropoutPrediction/Images/prediction.jpg);}\n""")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 120, 711, 291))
        self.frame.setStyleSheet("background-color: rgb(200, 130, 173);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 491, 41))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(540, 81, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(200, 188, 184);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(50, 210, 351, 41))
        self.comboBox.setStyleSheet("font: 75 14pt \"Malgun Gothic\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 170, 341, 41))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 361, 21))
        self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 205, 211, 53))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 91, 76);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Berlin Sans FB Demi\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(120, 410, 711, 121))
        self.frame_2.setStyleSheet("background-color: rgb(182, 162, 200);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 171, 71))
        self.label_3.setStyleSheet("font: 19pt \"Franklin Gothic Heavy\";")
        self.label_3.setObjectName("label_3")
        self.res = QtWidgets.QLabel(self.frame_2)
        self.res.setGeometry(QtCore.QRect(390, 30, 131, 51))
        self.res.setStyleSheet("font: 19pt \"Franklin Gothic Heavy\";\n"
"font: 26pt \"Algerian\";\n"
"color: rgb(200, 20, 68);")
        self.res.setFrameShape(QtWidgets.QFrame.Box)
        self.res.setLineWidth(1)
        self.res.setText("")
        self.res.setAlignment(QtCore.Qt.AlignCenter)
        self.res.setObjectName("res")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 2, 351, 51))
        self.label_5.setStyleSheet("font: 19pt \"Franklin Gothic Heavy\";\n"
"color: rgb(94, 47, 0);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2.clicked.connect(self.prediction)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Choose"))
        self.comboBox.setItemText(0, _translate("Dialog", "-------------Select --------------"))
        self.comboBox.setItemText(1, _translate("Dialog", "Decision Tree Classifier"))
        self.comboBox.setItemText(2,_translate("Dialog", "Gaussian Naive Bayes"))
        self.label.setText(_translate("Dialog", "Select The Algorithm*"))
        self.label_2.setText(_translate("Dialog", "Select the Testing File*"))
        self.pushButton_2.setText(_translate("Dialog", "Predict"))
        self.label_3.setText(_translate("Dialog", "DropOut   :"))
        self.label_5.setText(_translate("Dialog", "Dropout Prediction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Prediction()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

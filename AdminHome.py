from PyQt5 import QtCore, QtGui, QtWidgets
from Preprocessing import build_model
from DropoutPrediction import Ui_Prediction
from PerformanceTable import Ui_performance
from PerformanceEvaluation import performace


class Ui_Admin(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def Preprocessing(self):
        build_model()
        self.alertmsg("Successfull","DT and NB Model Build Successfully")
    def prediction(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Prediction()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def analysis(self):
        try:
            data = performace()
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_performance()
            self.ui.setupUi(self.Dialog)
            self.ui.view(data)
            self.Dialog.show()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print("LINE NO: ", tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setStyleSheet("QDialog{background-image: url(../DropoutPrediction/Images/admin.jpg);}\n""")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 200, 231, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(213, 59, 93);\n"
"font: 87 15pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 310, 231, 62))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(213, 59, 93);\n"
"font: 87 14pt \"Arial Black\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 420, 231, 63))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(213, 59, 93);\n"
"font: 87 14pt \"Arial Black\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 301, 41))
        self.label.setStyleSheet("font: 16pt \"Myanmar Text\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.Preprocessing)
        self.pushButton_2.clicked.connect(self.prediction)
        self.pushButton_3.clicked.connect(self.analysis)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Preprocessing"))
        self.pushButton_2.setText(_translate("Dialog", "Dropout\n"
"Prediction"))
        self.pushButton_3.setText(_translate("Dialog", "Performance\n"
"Evaluation"))
        self.label.setText(_translate("Dialog", "Welcome Admin..."))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

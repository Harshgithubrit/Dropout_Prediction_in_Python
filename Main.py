from PyQt5 import QtCore, QtGui, QtWidgets
from AdminHome import Ui_Admin


class Ui_Login(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def login(self):
        uid = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if uid == "" or uid == "null" or pwd=="" or pwd=="null":
           self.alertmsg("Error","Enter UserId and Password")
        elif uid == "admin" and pwd=="admin":
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Admin()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        else:
            self.alertmsg("Failed","Invalid Credentials")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setStyleSheet("QDialog{background-image: url(../DropoutPrediction/Images/mainbck.jpg);}\n"
"")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(360, 170, 371, 431))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(110, 110, 110, 184), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 20, 171, 51))
        self.label.setStyleSheet("background-color: rgb(213, 59, 93);\n"
"font: 24pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(56, 123, 270, 39))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(57, 202, 270, 39))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 300, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(213, 59, 93);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 921, 111))
        self.label_2.setStyleSheet("font: 25pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "LogIn"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "UserID"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "PassWord"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Higher Education Student Dropout Prediction and\n"
"Analysis through Educational Data Mining"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

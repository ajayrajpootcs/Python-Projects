# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvishUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1487, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1761, 1021))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/wallpaper2you_347368.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 90, 591, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/smile_loader_by_gleb.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 461, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/e8c5b61a18d49c20c48f0fe6d4839def4a96d970r1-444-250_hq.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 570, 491, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/team.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 490, 121, 201))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/me.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(880, 70, 251, 331))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/Private GIF.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(520, 70, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(690, 70, 181, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 310, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1050, 340, 261, 321))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/apna/Downloads/GRAPHICS DESIGNING/See every Iron Man suit from the Marvel movies in a single GIF.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1487, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "S  T  A  R  T"))
        self.pushButton_2.setText(_translate("MainWindow", "E  X  I  T"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 648)

        self.chance = 'X'
        self.turn = 0
        self.mw = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(150, 40, 231, 20))
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(150, 70, 231, 20))
        self.input2.setObjectName("input2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 141, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(300, 100, 75, 23))
        #self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 47, 13))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 380, 361, 71))
        self.result.setObjectName("result")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(80, 150, 71, 61))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(160, 150, 71, 61))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(240, 150, 71, 61))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(80, 220, 71, 61))
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(160, 222, 71, 61))
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(240, 222, 71, 61))
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(80, 290, 71, 61))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(160, 290, 71, 61))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(240, 290, 71, 61))
        self.btn9.setObjectName("btn9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn1.clicked.connect(self.changebtn1)
        self.btn2.clicked.connect(self.changebtn2)
        self.btn3.clicked.connect(self.changebtn3)
        self.btn4.clicked.connect(self.changebtn4)
        self.btn5.clicked.connect(self.changebtn5)
        self.btn6.clicked.connect(self.changebtn6)
        self.btn7.clicked.connect(self.changebtn7)
        self.btn8.clicked.connect(self.changebtn8)
        self.btn9.clicked.connect(self.changebtn9)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Enter your name Player1 :"))
        self.label_2.setText(_translate("MainWindow", "t!ctactoe game"))
        self.label_4.setText(_translate("MainWindow", "Enter your name Player2 :"))
        self.combination = [[self.btn1, self.btn2, self.btn3], [self.btn4, self.btn5, self.btn6],
                            [self.btn7, self.btn8, self.btn9], [self.btn1, self.btn4, self.btn7],
                            [self.btn2, self.btn5, self.btn8], [self.btn3, self.btn6, self.btn9],
                            [self.btn1, self.btn5, self.btn9], [self.btn3, self.btn5, self.btn7]]

    def changebtn1(self):
        text = self.changeValue(self.btn1)

    def changebtn2(self):
        text = self.changeValue(self.btn2)

    def changebtn3(self):
        text = self.changeValue(self.btn3)

    def changebtn4(self):
        text = self.changeValue(self.btn4)

    def changebtn5(self):
        text = self.changeValue(self.btn5)

    def changebtn6(self):
        text = self.changeValue(self.btn6)

    def changebtn7(self):
        text = self.changeValue(self.btn7)

    def changebtn8(self):
        text = self.changeValue(self.btn8)

    def changebtn9(self):
        text = self.changeValue(self.btn9)


    def changeValue(self, btn):
        player1 = self.input1.text()
        player2 = self.input2.text()
        if player1 and player2:

            text = btn.text()

            if "X" in text or "O" in text:
                pass
            else:
                btn.setText(self.chance)
                if "X" in self.chance:
                    self.chance = "O"
                else:
                    self.chance = "X"
            self.turn += 1
            if self.turn > 4:
                check = self.checker(btn)
                is_winner = self.checker(btn)
                if is_winner:
                    if 'O' in self.chance:
                        self.result.setPlainText(f'winner is {player1}')
                        return
                    else:
                        self.result.setPlainText(f'winner is {player2}')
                        return



            if self.turn == 9:
                self.result.setPlainText('noone wins the games...GAME OVER')
                return
        else:
            self.result.setPlainText("please fill names...")

    def checker(self, btn):
        value = btn.text()
        for row in self.combination:
            if btn in row:
                flag = True
                for item in row:
                    if value == item.text():
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    return True
        return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

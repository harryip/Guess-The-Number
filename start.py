from PyQt5.QtGui import QKeyEvent
from mainpage import Ui_Control
from NumRange_d import Ui_Range
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QLabel,QVBoxLayout
from PyQt5 import QtWidgets
import sys
import random
import pyttsx3
from PyQt5 import QtCore

class mainpage(QMainWindow, Ui_Control):
    def __init__(self,parent = None):
        super(mainpage, self).__init__(parent)
        self.setupUi(self)
        self.Start_Button.clicked.connect(self.start)
        self.engine = pyttsx3.init()

    def start(self):
        self.child = NumRange(self)
        self.child.show()
        Ans = random.randint(1, 99)
        self.c_num.display(Ans)
        self.child.OK_button.clicked.connect(self.enter)

    def enter(self):
        try:
            input = int(self.child.guess_num.text())
        except:
            input = 0
        c_ans = self.c_num.value()
        l_num = self.child.l_num.value()
        r_num = self.child.r_num.value()
        if input <= l_num or input >= r_num or input == 0:
            QMessageBox.about(self.child,"輸入數字錯誤" ,"請重新輸入數字")
            self.child.guess_num.setText('')
        else:
            if input == c_ans:
                QMessageBox.about(self.child,"恭喜" ,"恭喜猜中數字")
                self.child.close()
            else:
                self.child.guess_num.setText('')
                voices =self.engine.getProperty('voices')
                self.engine.setProperty("voice",voices[2].id)
                self.engine.setProperty('rate',200)
                if input < c_ans:
                    self.child.l_num.display(input)
                    voice = str(input)+'到'+str(int(r_num))
                if input > c_ans:
                    self.child.r_num.display(input)
                    voice = str(int(l_num))+'到'+str(input)
                try:
                    self.engine.endLoop()
                except:
                    pass
                self.engine.say(voice)
                self.engine.runAndWait()

class NumRange(QtWidgets.QDialog, Ui_Range):
    def __init__(self,parent = None):
        super(NumRange, self).__init__(parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == 16777220:
            self.parent().enter()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = mainpage()
    myWin.show()
    sys.exit(app.exec_())

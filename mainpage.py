# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Control(object):
    def setupUi(self, Control):
        Control.setObjectName("Control")
        Control.resize(800, 400)
        Control.setMinimumSize(QtCore.QSize(800, 400))
        Control.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtWidgets.QWidget(Control)
        self.centralwidget.setObjectName("centralwidget")
        self.c_num = QtWidgets.QLCDNumber(self.centralwidget)
        self.c_num.setGeometry(QtCore.QRect(250, 40, 300, 180))
        self.c_num.setDigitCount(3)
        self.c_num.setObjectName("c_num")
        self.button_widget = QtWidgets.QWidget(self.centralwidget)
        self.button_widget.setGeometry(QtCore.QRect(280, 270, 241, 101))
        self.button_widget.setObjectName("button_widget")
        self.Start_Button = QtWidgets.QPushButton(self.button_widget)
        self.Start_Button.setGeometry(QtCore.QRect(70, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Start_Button.setFont(font)
        self.Start_Button.setObjectName("Start_Button")
        Control.setCentralWidget(self.centralwidget)

        self.retranslateUi(Control)
        QtCore.QMetaObject.connectSlotsByName(Control)

    def retranslateUi(self, Control):
        _translate = QtCore.QCoreApplication.translate
        Control.setWindowTitle(_translate("Control", "MainWindow"))
        self.Start_Button.setText(_translate("Control", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Control = QtWidgets.QMainWindow()
    ui = Ui_Control()
    ui.setupUi(Control)
    Control.show()
    sys.exit(app.exec_())

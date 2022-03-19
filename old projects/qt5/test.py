from PyQt5 import QtCore, QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(600, 400)
w.setWindowTitle("حقيبة الطالب")
w.setStyleSheet('background-color: #2C3E50')
w.setWindowIcon(QtGui.QIcon('p.png'))
w.show()
app.exec_()

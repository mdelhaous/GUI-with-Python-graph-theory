
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Interface import GUI

mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())
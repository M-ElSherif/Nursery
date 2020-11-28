import sys

from PyQt5 import QtWidgets

from Controller.MainController import MainController

app = QtWidgets.QApplication(sys.argv)
main_controller = MainController()
main_controller.show()
app.exec_()

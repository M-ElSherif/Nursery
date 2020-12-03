import sys

from PyQt5 import QtWidgets, QtCore

from gui.Ui_PopupDialog import Ui_DialogPopup


class DialogPopupView(QtWidgets.QMainWindow, Ui_DialogPopup):

    def __init__(self, controller, model=None):
        super().__init__()
        self.setupUi(self)
        self.dialog_popup_controller = controller


    def assignButtons(self):
        self.dlgOKCancel.accepted.connect()

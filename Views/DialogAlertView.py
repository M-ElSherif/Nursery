import sys

from PyQt5 import QtWidgets, QtCore

from Enums.DialogEnums import DialogEnums
from gui.Ui_DialogAlert import Ui_Dialog


class DialogAlertView(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.assignButtons()

    def assignButtons(self):
        self.dlgBtnYesNo.accepted.connect(self.accept)
        self.dlgBtnYesNo.rejected.connect(self.reject)

    def show_dialog(self, s: bool, popup_enum: int):
        if popup_enum == DialogEnums.save_student.value:
            self.lblDialogAlert.setText("Student saved successfully!")
        elif popup_enum == DialogEnums.edit_student.value:
            self.lblDialogAlert.setText("Student updated successfully!")
        elif popup_enum == DialogEnums.delete_student_success.value:
            self.lblDialogAlert.setText("Student deleted successfully!")
        elif popup_enum == DialogEnums.delete_student_alert.value:
            self.lblDialogAlert.setText("Are you sure you wish to delete the student?")
        self.show()

    def reject(self, s=None):
        self.hide()

    def accept(self, s=None):
        self.hide()

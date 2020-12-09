import sys

from PyQt5 import QtWidgets, QtCore

from Enums.DialogEnums import DialogEnums
from gui.Ui_DialogConfirmation import Ui_Dialog


class DialogConfirmationView(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.assignButtons()

    def assignButtons(self):
        self.dlgBtnOkCancel.accepted.connect(self.accept)
        self.dlgBtnOkCancel.rejected.connect(self.reject)

    def show_dialog(self, s: bool, popup_enum: int):
        if popup_enum == DialogEnums.save_student.value:
            self.lblDialogConfirm.setText("Student saved successfully!")
        elif popup_enum == DialogEnums.edit_student.value:
            self.lblDialogConfirm.setText("Student updated successfully!")
        elif popup_enum == DialogEnums.delete_student_success.value:
            self.lblDialogConfirm.setText("Student deleted successfully!")
        elif popup_enum == DialogEnums.delete_student_alert.value:
            self.lblDialogConfirm.setText("Are you sure you wish to delete the student?")
        self.show()

    def accept(self, s=None):
        self.hide()

    def reject(self, s=None):
        self.hide()

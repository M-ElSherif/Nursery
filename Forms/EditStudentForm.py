from PyQt5.QtWidgets import QWidget
from gui.FormEditDeleteStudent import Ui_FormEditDeleteStudent

'''
EDIT / DELETE STUDENT FORM CLASS
'''


class EditDeleteStudentForm(QWidget, Ui_FormEditDeleteStudent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

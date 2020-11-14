from PyQt5.QtWidgets import QWidget

from gui.FormAddStudent import Ui_FormAddStudent

''' 
ADD STUDENT FORM CLASS
'''


class AddStudentForm(QWidget, Ui_FormAddStudent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

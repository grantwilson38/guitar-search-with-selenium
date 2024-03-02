
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Guitar Search")

        self.layout = QVBoxLayout(self)

        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(self.lineEdit)

        self.doneButton = QPushButton("Done", self)
        self.doneButton.clicked.connect(self.accept)
        self.layout.addWidget(self.doneButton)

    def textValue(self):
        return self.lineEdit.text()
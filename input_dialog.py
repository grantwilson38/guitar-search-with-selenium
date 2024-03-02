from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal

class InputDialog(QDialog):
    add_another = pyqtSignal(str)
    add_many = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Guitar Search")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Enter a guitar you are looking for:", self)
        self.layout.addWidget(self.label)

        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(self.lineEdit)

        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.add)
        self.layout.addWidget(self.addButton)

        self.importButton = QPushButton("Import from List", self)
        self.importButton.clicked.connect(self.import_guitars)
        self.layout.addWidget(self.importButton)

    def add(self):
        text = self.lineEdit.text()
        if text:  # only emit signal if text is not empty
            self.add_another.emit(text)
            self.lineEdit.clear()  # clear the lineEdit for the next input

    def import_guitars(self):
        with open('guitars.txt', 'r') as f:
            guitars = [line.strip() for line in f]
            self.add_many.emit(guitars)
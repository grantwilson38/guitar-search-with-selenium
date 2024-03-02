from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QListWidget

class InputDialog(QDialog):
    add_another = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Guitar Search")

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Enter a guitar you are looking for, or click 'Done' to finish:", self)
        self.layout.addWidget(self.label)

        self.lineEdit = QLineEdit(self)
        self.layout.addWidget(self.lineEdit)

        self.addButton = QPushButton("Add Another", self)
        self.addButton.clicked.connect(self.add_another_guitar)
        self.layout.addWidget(self.addButton)

        self.guitar_list = QListWidget(self)
        self.layout.addWidget(self.guitar_list)

        self.doneButton = QPushButton("Done", self)
        self.doneButton.clicked.connect(self.close_dialog)
        self.layout.addWidget(self.doneButton)

    def textValue(self):
        return self.lineEdit.text()

    def add_another_guitar(self):
        guitar = self.textValue().strip()
        if guitar:
            self.add_another.emit(guitar)
            self.guitar_list.addItem(guitar)
        self.lineEdit.clear()

    def close_dialog(self):
        self.doneButton.clicked.disconnect()
        self.close()
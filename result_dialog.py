from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QFrame

class ResultDialog(QDialog):
    def __init__(self, found_guitars, not_found_guitars, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Search Results")
        self.resize(600, 400)  # Resize the dialog box

        self.layout = QHBoxLayout(self)  # Use QHBoxLayout to separate the lists into two columns

        # Found guitars column
        found_layout = QVBoxLayout()
        found_label = QLabel("<b>Found Guitars:</b>", self)  # Use HTML to make the title bold
        found_layout.addWidget(found_label)

        for guitar in found_guitars:
            found_layout.addWidget(QLabel(guitar, self))

        # Add a vertical line
        vertical_line = QFrame(self)
        vertical_line.setFrameShape(QFrame.VLine)
        vertical_line.setFrameShadow(QFrame.Sunken)

        # Not found guitars column
        not_found_layout = QVBoxLayout()
        not_found_label = QLabel("<b>Not Found Guitars:</b>", self)  # Use HTML to make the title bold
        not_found_layout.addWidget(not_found_label)

        for guitar in not_found_guitars:
            not_found_layout.addWidget(QLabel(guitar, self))

        # Add the columns to the main layout
        self.layout.addLayout(found_layout)
        self.layout.addWidget(vertical_line)
        self.layout.addLayout(not_found_layout)

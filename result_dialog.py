from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QWidget

class ResultDialog(QDialog):
    def __init__(self, found_guitars, not_found_guitars, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Search Results")

        self.layout = QHBoxLayout(self)

        # Found guitars column
        found_layout = QVBoxLayout()
        found_label = QLabel("<b>Found Guitars:</b>", self)
        found_layout.addWidget(found_label)

        # Add the guitars to the layout
        for guitar in found_guitars:
            found_layout.addWidget(QLabel(guitar, self))

        found_scroll = QScrollArea(self)
        found_widget = QWidget(self)
        found_widget.setLayout(found_layout)
        found_scroll.setWidget(found_widget)
        self.layout.addWidget(found_scroll)

        # Not found guitars column
        not_found_layout = QVBoxLayout()
        not_found_label = QLabel("<b>Not Found Guitars:</b>", self)
        not_found_layout.addWidget(not_found_label)

        # Add the guitars to the layout
        for guitar in not_found_guitars:
            not_found_layout.addWidget(QLabel(guitar, self))

        not_found_scroll = QScrollArea(self)
        not_found_widget = QWidget(self)
        not_found_widget.setLayout(not_found_layout)
        not_found_scroll.setWidget(not_found_widget)
        self.layout.addWidget(not_found_scroll)

        # Make the layout adjust its size to fit its contents
        self.layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
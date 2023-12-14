import sys 
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Greeting_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText('Your Name:')
        vbox.addWidget(self.label)
        self.name_entry = QLineEdit(self)
        vbox.addWidget(self.name_entry)
        pbt = QPushButton("Go!", self)
        pbt.clicked.connect(self.greet)
        vbox.addWidget(pbt)
        self.setLayout(vbox)
        self.show()

    def greet(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText('Hello, ' + self.name_entry.text())
        layout.addWidget(label)
        close_button = QPushButton('Close window', self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    w = Greeting_window()
    sys.exit(app.exec())
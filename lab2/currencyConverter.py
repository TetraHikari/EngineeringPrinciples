import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Greeting_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Thai Baht to US Dollar Converter")
        vbox.addWidget(self.label)
        self.money_entry = QLineEdit(self)
        vbox.addWidget(self.money_entry)
        pbt = QPushButton("Baht to Dollar", self)
        pbt.clicked.connect(self.baht_converter)
        vbox.addWidget(pbt)

        pbt = QPushButton("Dollar to Baht", self)
        pbt.clicked.connect(self.dollar_converter)
        vbox.addWidget(pbt)

        self.setLayout(vbox)
        self.show()

    def baht_converter(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("US Dollar = " + str(float(self.money_entry.text()) / 30) + " Dollar")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def dollar_converter(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Thai Baht = " + str(float(self.money_entry.text()) * 30) + " Baht")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Greeting_window()
    sys.exit(app.exec_())
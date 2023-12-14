import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Simple_spin_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)
        plus = QPushButton('+', self)
        plus.clicked.connect(self.updatNumber)
        vbox.addWidget(plus)
        minus = QPushButton('-', self)
        minus.clicked.connect(self.updatNumber)
        vbox.addWidget(minus)
        reset = QPushButton('Reset', self)
        reset.clicked.connect(self.resetNumbr)
        vbox.addWidget(reset)
        self.setLayout(vbox)
        self.show()

    def updatNumber(self):
        text = self.sender().text()
        if text == '+':
            self.num += 1
        else:
            self.num -= 1
        self.label.setText(str(self.num))

    def resetNumbr(self):
        self.num = 0
        self.label.setText(str(self.num))

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    w = Simple_spin_window()
    sys.exit(app.exec())
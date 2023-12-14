import sys
from PySide6.QtWidgets import *

#display a message box
def say_hello():
    msg = QMessageBox()
    msg.setText('Hello World!')
    msg.exec()
    



if __name__ == '__main__' :
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Simple')
    btn = QPushButton('Say hello!', w)
    btn.clicked.connect(say_hello)
    w.show()

    sys.exit(app.exec())
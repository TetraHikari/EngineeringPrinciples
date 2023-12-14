import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from program3_3 import Ui_Form
from dail import Ui_Form as Ui_Form2

class PhoneApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect numeric buttons to a common function
        numeric_buttons = [self.ui.b1, self.ui.b2, self.ui.b3, self.ui.b4, self.ui.b5, self.ui.b6, self.ui.b7, self.ui.b8, self.ui.b9, self.ui.b0, self.ui.bstar, self.ui.bhash]
        for button in numeric_buttons:
            button.clicked.connect(self.numeric_button_clicked)

        # Connect other buttons
        self.ui.btalk.clicked.connect(self.talk_clicked)
        self.ui.bdel.clicked.connect(self.delete_clicked)

        # Initialize current_number
        self.current_number = ""

    def numeric_button_clicked(self):
        # Add your functionality when a numeric button is clicked
        sender = self.sender()
        if sender:
            text = sender.text()
            self.current_number += text
            self.ui.lineEdit.setPlainText(self.current_number)

    def talk_clicked(self):
        # Open Ui_Form2 and display the current number
        dialog = QDialog()
        ui_form2 = Ui_Form2()
        ui_form2.setupUi(dialog)
        ui_form2.labeldail.setText("Dialing " + self.current_number)
        dialog.exec_()

    def delete_clicked(self):
        # Add your functionality when the "Delete" button is clicked
        self.current_number = self.current_number[:-1] if self.current_number else self.current_number
        self.ui.lineEdit.setPlainText(self.current_number)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneApp()
    window.show()
    sys.exit(app.exec_())

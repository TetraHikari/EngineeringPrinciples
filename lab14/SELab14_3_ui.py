import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Traffic Light Demo")
        self.setGeometry(100, 100, 300, 100)

        self.setup_ui()

        # Initial state
        self.current_color = "red"
        self.setTimer(4)

    def setup_ui(self):
        layout = QGridLayout()

        self.button_red = QPushButton("")
        self.button_red.clicked.connect(self.flash_red)
        layout.addWidget(self.button_red, 0, 0)

        self.button_yellow = QPushButton("")
        self.button_yellow.clicked.connect(self.flash_yellow)
        layout.addWidget(self.button_yellow, 0, 1)

        self.button_green = QPushButton("")
        self.button_green.clicked.connect(self.flash_green)
        layout.addWidget(self.button_green, 0, 2)

        self.label_number = QLabel("Time: 0")
        layout.addWidget(self.label_number, 1, 0, 1, 3)

        self.button_tick = QPushButton("Tick")
        self.button_tick.clicked.connect(self.tick)
        layout.addWidget(self.button_tick, 2, 0, 1, 3)


        self.setLayout(layout)

        # Timer to update the number every second
        self.number = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_number)
        self.timer.start(1000)

    def setTimer(self, seconds):
        self.timer.stop()
        self.number = 0
        self.timer_interval = seconds
        self.timer.start(1000)

    def changeColor(self, color):
        if color == "red":
            self.flash_red()
        elif color == "yellow":
            self.flash_yellow()
        elif color == "green":
            self.flash_green()

    def flash_red(self):
        self.button_red.setStyleSheet("background-color: #FF0000")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: None")
        self.current_color = "red"
        QApplication.processEvents()

    def flash_yellow(self):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: #FFFF00")
        self.button_green.setStyleSheet("background-color: None")
        self.current_color = "yellow"
        QApplication.processEvents()

    def flash_green(self):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: #00FF00")
        self.current_color = "green"
        QApplication.processEvents()

    def update_number(self):
        self.number += 1
        self.label_number.setText("Time: {}".format(self.number))

        if self.number == self.timer_interval:
            if self.current_color == "red":
                self.setTimer(3)
                self.changeColor("green")
            elif self.current_color == "green":
                self.setTimer(2)
                self.changeColor("yellow")
            elif self.current_color == "yellow":
                self.setTimer(4)
                self.changeColor("red")

    def tick(self):
        if self.number > 0:
            self.number -= 1
            self.label_number.setText("Time: {}".format(self.number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

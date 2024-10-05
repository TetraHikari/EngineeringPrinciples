import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Traffic Light Demo")
        self.setGeometry(100, 100, 300, 150)

        self.setup_ui()

        # Traffic light attributes
        self.state = "red"
        self.duration = {"red": 4, "green": 3, "yellow": 2}
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_state)
        self.timer.start(1000)  # 1000 ms = 1 second

    def setup_ui(self):
        layout = QGridLayout()

        self.button_red = QPushButton("Red")
        self.button_red.clicked.connect(lambda: self.changeColor("red"))
        layout.addWidget(self.button_red, 0, 0)

        self.button_yellow = QPushButton("Yellow")
        self.button_yellow.clicked.connect(lambda: self.changeColor("yellow"))
        layout.addWidget(self.button_yellow, 0, 1)

        self.button_green = QPushButton("Green")
        self.button_green.clicked.connect(lambda: self.changeColor("green"))
        layout.addWidget(self.button_green, 0, 2)

        self.label_number = QLabel("Time: 0")
        layout.addWidget(self.label_number, 1, 0, 1, 3)

        self.setLayout(layout)

        # Timer to update the number every second
        self.number = 0
        self.timer_number = QTimer(self)
        self.timer_number.timeout.connect(self.update_number)
        self.timer_number.start(1000)  # 1000 ms = 1 second

    def changeColor(self, color):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: None")

        if color == "red":
            self.button_red.setStyleSheet("background-color: #FF0000")
            print("Red")
        elif color == "yellow":
            self.button_yellow.setStyleSheet("background-color: #FFFF00")
            print("Yellow")
        elif color == "green":
            self.button_green.setStyleSheet("background-color: #00FF00")
            print("Green")

    def update_state(self):
        if self.duration[self.state] > 0:
            self.duration[self.state] -= 1

        if self.duration[self.state] == 0:
            if self.state == "red":
                self.state = "green"
                print("Green")
            elif self.state == "green":
                self.state = "yellow"
                print("Yellow")
            elif self.state == "yellow":
                self.state = "red"
                print("Red")

            self.duration[self.state] -= 1

        self.update_traffic_light()

    def update_traffic_light(self):
        self.button_red.setStyleSheet("background-color: None")
        self.button_yellow.setStyleSheet("background-color: None")
        self.button_green.setStyleSheet("background-color: None")

        if self.state == "red":
            self.button_red.setStyleSheet("background-color: #FF0000")
            print("Red")
        elif self.state == "yellow":
            self.button_yellow.setStyleSheet("background-color: #FFFF00")
            print("Yellow")
        elif self.state == "green":
            self.button_green.setStyleSheet("background-color: #00FF00")
            print("Green")

        QApplication.processEvents()

    def update_number(self):
        self.number += 1
        self.label_number.setText("Time: {}".format(self.number))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    traffic_light = TrafficLight()
    traffic_light.show()
    sys.exit(app.exec())

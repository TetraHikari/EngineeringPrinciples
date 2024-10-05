import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.frame_no = 0
        self.paused = False  # Initialize the paused attribute
        self.images = [QPixmap("images/frame-" + str(i + 1) + ".png") for i in range(20)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value) # Connect the timer to the update_value method
        self.timer.start(75)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        if not self.paused:
            self.frame_no += 1
            self.frame_no %= 20
            self.update()
            if self.frame_no == 0:
                self.QSE.play()
            self.update()

    def pause_animation(self):
        self.paused = not self.paused
        if self.paused:
            self.timer.stop()
        else:
            self.timer.start(75)

class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.anim_area.pause_animation)

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        layout.addWidget(self.pause_button)
        self.setLayout(layout)
        self.setMinimumSize(350, 400)

def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

from operator import is_
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class Dinosaur:
    def __init__(self):
        self.image = QPixmap("images/dinosaur.png") 
        self.jump_sound = QSoundEffect()
        self.jump_sound.setSource(QUrl.fromLocalFile("sounds/sound2.wav"))
        self.x = 50
        self.y = 300
        self.w = 40
        self.h = 40
        self.is_jumping = False
        self.jump_speed = 15

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def jump(self):
        if not self.is_jumping:
            print("Jump!")
            self.jump_sound.play()
            self.is_jumping = True

    def update_position(self):
        if self.is_jumping:
            self.y -= self.jump_speed
            self.jump_speed -= 1  # gravity

            # Check if the dinosaur has reached the ground
            if self.y >= 300:
                self.y = 300
                self.is_jumping = False
                self.jump_speed = 15
        else:
            # Reset the jump speed if not jumping
            self.jump_speed = 15

class Obstacle:
    def __init__(self):
        self.image = QPixmap("images/spike.png") 
        self.x = 500
        self.y = 300
        self.w = 40
        self.h = 40
        self.speed = 5

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def move(self):
        self.x -= self.speed
        if self.x < -self.w:
            self.x = 550  # Reposition off-screen

class GameArea(QWidget):
    game_over_changed = Signal()
    game_not_over_changed = Signal()

    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(600, 400)
        self.dino = Dinosaur()
        self.obstacle = Obstacle()
        self.score = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(20)
        self.setFocusPolicy(Qt.StrongFocus)
        self.game_over = False  

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            self.dino.jump()

    def paintEvent(self, e):
        buffer = QPixmap(self.size())
        buffer.fill(Qt.white)
        p = QPainter(buffer)
        self.dino.draw(p)
        self.obstacle.draw(p)
        self.draw_score(p)

        if self.game_over:
            self.draw_game_over(p) 

        p.end()

        painter = QPainter(self)
        painter.drawPixmap(0, 0, buffer)

    def draw_score(self, painter):
        font = QFont("Arial", 12)
        painter.setFont(font)
        painter.setPen(Qt.black)
        painter.drawText(self.width() - 80, 20, f"Score: {self.score}")

    def update_game(self):
        if not self.game_over:
            self.dino.update_position()
            self.obstacle.move()
            self.check_collision()
            self.update()

    def check_collision(self):
        if (
            self.dino.x < self.obstacle.x + self.obstacle.w
            and self.dino.x + self.dino.w > self.obstacle.x
            and self.dino.y < self.obstacle.y + self.obstacle.h
            and self.dino.y + self.dino.h > self.obstacle.y
        ):
            print("Game Over!")
            self.game_over = True
            self.timer.stop()
            self.game_over_changed.emit() 
            self.update()
        else:
            if self.dino.x > self.obstacle.x + self.obstacle.w:
                self.score += 1 

    def draw_game_over(self, painter):
        font = QFont("Arial", 20)
        painter.setFont(font)
        painter.setPen(Qt.black)
        painter.drawText(self.width() // 2 - 100, self.height() // 2 - 20, "Game Over")

        if self.game_over:
            self.play_again_button.show()  
        else:
            self.play_again_button.hide() 

    def reset_game(self):
        self.game_over = False
        self.score = 0
        self.dino = Dinosaur()
        self.obstacle = Obstacle()
        self.timer.start()
        self.game_not_over_changed.emit()
        self.update()

    def showEvent(self, event):
        self.play_again_button = QPushButton("Play Again", self)
        self.play_again_button.clicked.connect(self.reset_game)
        self.game_over_changed.connect(self.play_again_button.show)
        self.game_not_over_changed.connect(self.play_again_button.hide)
        self.play_again_button.setStyleSheet("color: black;") 
        self.adjust_button_placement()

    def adjust_button_placement(self):
        self.play_again_button.move(
            self.width() // 2 - self.play_again_button.width() // 2,
            self.height() // 2 - self.play_again_button.height() // 2,
        )


class GameWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.game_area = GameArea()
        layout = QVBoxLayout()
        layout.addWidget(self.game_area)
        self.setLayout(layout)
        self.setMinimumSize(600, 400)


def main():
    app = QApplication(sys.argv)
    w = GameWindow()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())

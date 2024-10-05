import js
from pyscript import document, window
from abc import ABC, abstractmethod
import random

class AbstractWidget(ABC):
    def __init__(self, container):
        self.container = container

    @abstractmethod
    def draw(self):
        pass

class GameWidget(AbstractWidget):
    def __init__(self, container):
        super().__init__(container)
        self.score = 0
        self.ball = None
        self.score_display = document.createElement("p")
        self.container.appendChild(self.score_display)
        self.update_score_display()
        self.clicked_sound =  js.Audio.new("sounds/sound2.mp3")

    def draw(self):
        self.draw_ball()
        self.start_moving_ball()

    def draw_ball(self):
        if self.ball:
            self.container.removeChild(self.ball)
        self.ball = document.createElement("div")
        self.ball.style.width = "50px"
        self.ball.style.height = "50px"
        self.ball.style.borderRadius = "50%"
        self.ball.style.position = "absolute"
        self.ball.style.backgroundColor = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
        self.ball.onclick = self.ball_clicked
        self.container.appendChild(self.ball)
        self.move_ball() 

    def move_ball(self):
        container_width = self.container.clientWidth
        container_height = self.container.clientHeight
        new_left = random.randint(0, container_width - 50) 
        new_top = random.randint(0, container_height - 50)  
        self.ball.style.left = f"{new_left}px"
        self.ball.style.top = f"{new_top}px"

    def start_moving_ball(self):
        move_interval = 1000  
        js.setInterval(self.move_ball, move_interval)

    def ball_clicked(self, event):
        self.score += 1
        self.update_score_display()
        self.ball.style.backgroundColor = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
        self.clicked_sound.play()
        self.move_ball()


    def update_score_display(self):
        self.score_display.innerText = f"Score: {self.score}"

if __name__ == "__main__":
    container = document.querySelector("#container")
    game_widget = GameWidget(container)
    game_widget.draw()

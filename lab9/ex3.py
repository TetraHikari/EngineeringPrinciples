import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
import random


class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        """ Return the dom element """
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element

    @abstractmethod
    def drawWidget(self):
        pass

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.paused = False

    def on_click(self, event):
        self.paused = not self.paused
        self.button.innerText = "play" if self.paused else "pause"

    def on_setInterval(self):
        if not self.paused:
            self.counter += 1
            if self.counter > 20:
                self.jump_sound.play()
                self.counter = 1
            self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)
        self.counter = 1
        self.paused = False

    def on_click(self, event):
        self.paused = not self.paused
        self.button.innerText = "play" if self.paused else "pause"

    def on_setInterval(self):
        if not self.paused:
            self.counter += 1
            if self.counter > 20:
                self.jump_sound.play()
                self.counter = 1
            self.image.src = "./images/frame-" + str(self.counter) + ".png"
            self.image.style.filter = "hue-rotate(" + str(self.counter * 18) + "deg)"

    # adding a random color button which randomizes a background color for the background
    def on_random_color(self, event):
        self.element.style.backgroundColor = "rgb(" + str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) + ")"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)
        self.random_color_button = document.createElement("button")
        self.random_color_button.innerText = "random color"
        self.random_color_button.style.width = "600px"
        self.random_color_button.onclick = create_proxy(self.on_random_color)
        self.element.appendChild(self.random_color_button)

class

    

 
if __name__ == "__main__":
    animation_widget = ColorfulAnimationWidget("animation")
    animation_widget.drawWidget()

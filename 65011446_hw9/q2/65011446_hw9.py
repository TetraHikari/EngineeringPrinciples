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

    def update_attribute(self):
        pass

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)
        self.counter = 1
        self.paused = False

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

class WidgetContainer:
    def __init__(self, container_id):
        self.container_id = container_id
        self.widgets = []

    def add_widget(self, widget):
        """Add a widget to the container."""
        if not issubclass(widget.__class__, AbstractWidget):
            raise ValueError("widget must be a subclass of AbstractWidget")
        self.widgets.append(widget)

    def draw_widgets(self):
        """Draw all widgets in the container."""
        container_element = document.querySelector(f"#{self.container_id}")
        if not container_element:
            raise ValueError(f"Container with ID {self.container_id} not found")
        for widget in self.widgets:
            widget_element = document.createElement("div")
            widget_element.id = widget.element_id
            container_element.appendChild(widget_element)
            widget.drawWidget()

class AnimationSpeedWidget(AnimationWidget):
    def __init__(self, element_id):
        super().__init__(element_id) 
        self.speed = 100
        self.interval_id = None  
        self.image_width = "600px"
        self.image_height = "600px"

    def drawWidget(self):
        super().drawWidget() 
        self.speed_up_button = document.createElement("button")
        self.speed_up_button.innerText = "Speed Up"
        self.speed_up_button.style.width = "100px"
        self.speed_up_button.onclick = create_proxy(self.on_speed_up)
        self.element.appendChild(self.speed_up_button)

        self.speed_down_button = document.createElement("button")
        self.speed_down_button.innerText = "Speed Down"
        self.speed_down_button.style.width = "100px"
        self.speed_down_button.onclick = create_proxy(self.on_speed_down)
        self.element.appendChild(self.speed_down_button)

        # Initialize the animation with the default speed
        self.update_interval()

    def update_interval(self):
        if self.interval_id is not None:
            js.clearInterval(self.interval_id) 
        on_setInterval = create_proxy(self.on_setInterval)
        self.interval_id = js.setInterval(on_setInterval, self.speed)  

    def on_speed_up(self, event):
        self.speed = max(10, self.speed - 10)
        self.update_interval() 

    def on_speed_down(self, event):
        self.speed = min(1000, self.speed + 10)
        self.update_interval()  
    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, self.speed)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)
        self.speed_up_button = document.createElement("button")
        self.speed_up_button.innerText = "speed up"
        self.speed_up_button.style.width = "600px"
        self.speed_up_button.onclick = create_proxy(self.on_speed_up)
        self.element.appendChild(self.speed_up_button)
        self.speed_down_button = document.createElement("button")
        self.speed_down_button.innerText = "speed down"
        self.speed_down_button.style.width = "600px"
        self.speed_down_button.onclick = create_proxy(self.on_speed_down)
        self.element.appendChild(self.speed_down_button)

    def update_attribute(self):
        if self._element and hasattr(self, 'image'):  
            self.image.style.width = self.image_width
            self.image.style.height = self.image_height

class SliderControlWidget(AbstractWidget):
    def __init__(self, element_id, target_widget, attribute_name):
        super().__init__(element_id)
        self.target_widget = target_widget
        self.attribute_name = attribute_name 

    def on_slider_change(self, event):
        new_value = event.target.value 
        setattr(self.target_widget, self.attribute_name, f"{new_value}px")  
        self.target_widget.update_attribute()

    def drawWidget(self):
        self.slider = document.createElement("input")
        self.slider.setAttribute("type", "range")
        self.slider.setAttribute("min", "100")
        self.slider.setAttribute("max", "800")
        self.slider.setAttribute("value", "600")
        self.slider.style.width = "600px"
        self.slider.oninput = create_proxy(self.on_slider_change)
        self.element.appendChild(self.slider)

        self.label = document.createElement("span")
        self.label.innerText = f"Adjust {self.attribute_name}"
        self.element.appendChild(self.label)

class ResizableAnimationWidget(AnimationWidget):
    def update_attribute(self):
        if hasattr(self, 'image'):
            self.image.style.width = self.image_width
            self.image.style.height = self.image_height

    def drawWidget(self):
        super().drawWidget()
        self.image_width = "600px"
        self.image_height = "600px"
        self.update_attribute()

    
if __name__ == "__main__":
    container = WidgetContainer("widget_container")
    # animation_widget = ColorfulAnimationWidget("animation_widget")
    animation_widget = AnimationSpeedWidget("animation_widget")
    slider_widget = SliderControlWidget("slider_widget", animation_widget, "image_width")
    slider_widget2 = SliderControlWidget("slider_widget2", animation_widget, "image_height")
    
    
    container.add_widget(animation_widget)
    container.add_widget(slider_widget)
    container.add_widget(slider_widget2)
    container.draw_widgets()


import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod

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

class CurrencyConverterWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.conversion_rate = 30  # 1 USD = 30 THB

    def thb_to_usd(self, event):
        try:
            thb_amount = float(self.number_input.value)
            usd_amount = thb_amount / self.conversion_rate
            js.alert(f"{thb_amount} THB is equal to {usd_amount:.2f} USD")
        except ValueError:
            js.alert("Please enter a valid number")

    def usd_to_thb(self, event):
        try:
            usd_amount = float(self.number_input.value)
            thb_amount = usd_amount * self.conversion_rate
            js.alert(f"{usd_amount} USD is equal to {thb_amount:.2f} THB")
        except ValueError:
            js.alert("Please enter a valid number")
        

    def drawWidget(self):
        self.number_input = document.createElement("input", type="number")
        self.number_input.placeholder = "Enter a number"
        self.element.appendChild(self.number_input)

        self.convert_usd_to_thb_button = document.createElement("button")
        self.convert_usd_to_thb_button.innerText = "USD to THB"
        self.convert_usd_to_thb_button.onclick = create_proxy(self.usd_to_thb)
        self.element.appendChild(self.convert_usd_to_thb_button)

        self.convert_thb_to_usd_button = document.createElement("button")
        self.convert_thb_to_usd_button.innerText = "THB to USD"
        self.convert_thb_to_usd_button.onclick = create_proxy(self.thb_to_usd)
        self.element.appendChild(self.convert_thb_to_usd_button)

if __name__ == "__main__":
    converter = CurrencyConverterWidget("container")
    converter.drawWidget()

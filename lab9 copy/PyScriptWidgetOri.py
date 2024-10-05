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
            thb_amount = float(self.thb_input.value)
            usd_amount = thb_amount / self.conversion_rate
            js.alert(f"{thb_amount} THB is equal to {usd_amount:.2f} USD")
        except ValueError:
            js.alert("Please enter a valid number")

    def usd_to_thb(self, event):
        try:
            usd_amount = float(self.usd_input.value)
            thb_amount = usd_amount * self.conversion_rate
            js.alert(f"{usd_amount} USD is equal to {thb_amount:.2f} THB")
        except ValueError:
            js.alert("Please enter a valid number")

    def drawWidget(self):
        self.thb_input = document.createElement("input", type="number")
        self.thb_input.placeholder = "Amount in THB"
        self.element.appendChild(self.thb_input)

        self.thb_to_usd_button = document.createElement("button")
        self.thb_to_usd_button.innerText = "Convert THB to USD"
        self.thb_to_usd_button.onclick = create_proxy(self.thb_to_usd)
        self.element.appendChild(self.thb_to_usd_button)

        self.usd_input = document.createElement("input", type="number")
        self.usd_input.placeholder = "Amount in USD"
        self.element.appendChild(self.usd_input)

        self.usd_to_thb_button = document.createElement("button")
        self.usd_to_thb_button.innerText = "Convert USD to THB"
        self.usd_to_thb_button.onclick = create_proxy(self.usd_to_thb)
        self.element.appendChild(self.usd_to_thb_button)

if __name__ == "__main__":
    converter = CurrencyConverterWidget("container")
    converter.drawWidget()

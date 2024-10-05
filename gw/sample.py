import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtMultimedia import *
from PySide6.QtCore import QUrl

class ShoppingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping Application")

        self.shoppingCart = []

        # Initialize the media player for sound playback
        self.player = QMediaPlayer()

        self.setupUI()

    def setupUI(self):
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        layout = QVBoxLayout()

        self.itemsList = QListWidget()

        # Dictionary to hold product names and their corresponding image paths
        products = {
            "Apples": "./pic/apple.jpeg",
            "Bananas": "./pic/banana.png",
            "Oranges": "./pic/orange.png",
            "Milk": "pic/milk.png",
            "Bread": "pic/bread.png"
        }

        # Adding products to the list with images
        for product, imagePath in products.items():
            item = QListWidgetItem(product)
            item.setIcon(QIcon(imagePath))
            self.itemsList.addItem(item)

        layout.addWidget(self.itemsList)

        self.addItemButton = QPushButton("Add to Cart")
        self.addItemButton.clicked.connect(self.addItem)
        layout.addWidget(self.addItemButton)

        self.cartContentsLabel = QLabel("Cart: ")
        layout.addWidget(self.cartContentsLabel)

        self.clearCartButton = QPushButton("Clear Cart")
        self.clearCartButton.clicked.connect(self.clearCart)
        layout.addWidget(self.clearCartButton)

        mainWidget.setLayout(layout)

    def addItem(self):
        selectedItem = self.itemsList.currentItem()
        if selectedItem:
            self.shoppingCart.append(selectedItem.text())
            self.updateCartDisplay()
            self.playSound("path/to/add_sound.wav")  # Update this path to your sound file

    def clearCart(self):
        self.shoppingCart.clear()
        self.updateCartDisplay()

    def updateCartDisplay(self):
        self.cartContentsLabel.setText("Cart: " + ", ".join(self.shoppingCart))

    def playSound(self, soundPath):
        # Play the sound for adding an item
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(soundPath)))
        self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingApp()
    window.show()
    sys.exit(app.exec())

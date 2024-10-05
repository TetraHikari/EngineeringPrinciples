
        label = QLabel(self)
        label.setText("Thai Baht = " + str(float(self.money_entry.text()) * 30) + " Baht")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Greeting_window()
    sys.exit(app.exec_())
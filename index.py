from selenium import webdriver;
import time
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

PATH = "C:\Program Files (x86)\chromedriver.exe"


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                    alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        browser = webdriver.Chrome(PATH)
        browser.get("http://nike.com")
        time.sleep(5)

if __name__ == "__main__":
    
    

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 600)
    widget.show()

    sys.exit(app.exec_())

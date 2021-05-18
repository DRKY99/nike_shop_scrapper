from selenium import webdriver;
import time
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

#default path to chrome driver
BROWSER = "Chrome"
BROWSER_LIST =["Chrome","Firefox","Edge","Opera"]
PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "http://nike.com"
DELAY = 3
DELAY_LIST=range(10)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #browser
        self.browser_selector = QtWidgets.QComboBox()
        self.browser_selector.addItems(BROWSER_LIST)
        #driver path
        self.driver_path = QtWidgets.QLineEdit(PATH)
        #URL
        self.url_path = QtWidgets.QLineEdit(URL)
        #Delay
        self.delay_selector = QtWidgets.QComboBox()
        self.delay_selector.addItems([str(x) for x in DELAY_LIST])
        #run script
        self.run = QtWidgets.QPushButton("Run script")
        #build
        self.build()
    
    def build(self):
        self.layout = QtWidgets.QFormLayout(self)
        #==== widgets
        #browser
        self.layout.addRow("Select your browser",self.browser_selector)
        #driver path
        self.layout.addRow("Select your driver path",self.driver_path)
        #URL
        self.layout.addRow("Set the URL",self.url_path)
        #Delay
        self.layout.addRow("Select your delay",self.delay_selector)
        #run
        self.layout.addRow(self.run)
        #==== methods
        self.run.clicked.connect(self.runScript)

    @QtCore.Slot()
    def runScript(self):
        browser = webdriver.Chrome(PATH)
        browser.get(URL)
        time.sleep(DELAY)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 150)
    widget.show()

    sys.exit(app.exec_())

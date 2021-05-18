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

USER = "username"
PASSWORD = "password"

CARD_NUMBER = "XXXX XXXX XXXX XXXX"
CARD_CVV = "000"
CARD_DATE = "00/0"

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
        #credentials
        self.credentials_user = QtWidgets.QLineEdit(USER)
        self.credentials_pass = QtWidgets.QLineEdit(PASSWORD)
        #card
        self.card_number = QtWidgets.QLineEdit(CARD_NUMBER)
        self.card_date = QtWidgets.QLineEdit(CARD_DATE)
        self.card_cvv = QtWidgets.QLineEdit(CARD_CVV)
        #run script
        self.run = QtWidgets.QPushButton("Run script")
        #build
        self.build()
    
    def build(self):
        self.layout = QtWidgets.QFormLayout(self)
        #==== widgets
        #browser
        self.layout.addRow(QtWidgets.QLabel("Browser and driver"))
        self.layout.addRow("Select your browser",self.browser_selector)
        #driver path
        self.layout.addRow("Select your driver path",self.driver_path)
        #Delay
        self.layout.addRow(QtWidgets.QLabel("Delay"))
        self.layout.addRow("Select your delay",self.delay_selector)
        #URL
        self.layout.addRow(QtWidgets.QLabel("URL and credentials"))
        self.layout.addRow("Set the URL",self.url_path)
        #Credentials
        self.layout.addRow("Username",self.credentials_user)
        self.layout.addRow("Password",self.credentials_pass)
        #Card
        self.layout.addRow(QtWidgets.QLabel("Card data"))
        self.layout.addRow("Card number",self.card_number)
        self.layout.addRow("Card date",self.card_date)
        self.layout.addRow("Card cvv",self.card_cvv)
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

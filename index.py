from Manager import Manager
import os
import sys
import selenium
import json

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Signal, Slot, Property

from Manager import Manager

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__),"qml/index.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
    
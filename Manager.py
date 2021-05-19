from PySide6.QtCore import Qt, QObject, Signal, Slot, Property

class Manager(QObject):
    def __init__(self):
            QObject.__init__(self)
        
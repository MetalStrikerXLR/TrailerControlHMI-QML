from PyQt5.QtCore import QObject


class CameraCapture(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_cap = None
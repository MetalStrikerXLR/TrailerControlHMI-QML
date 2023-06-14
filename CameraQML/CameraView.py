from PyQt5.QtCore import pyqtSignal, pyqtProperty, QPoint
from PyQt5.QtGui import QImage
from PyQt5.QtQuick import QQuickPaintedItem


class CameraView(QQuickPaintedItem):
    imageChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(CameraView, self).__init__(parent)
        self.m_image = QImage()

    def paint(self, painter):
        if self.m_image.isNull():
            return

        image = self.m_image.scaled(self.size().toSize())
        painter.drawImage(QPoint(), image)

    def image(self):
        return self.m_image

    def setImage(self, image):
        if self.m_image == image:
            return

        self.m_image = image
        self.imageChanged.emit()
        self.update()

    image = pyqtProperty(QImage, fget=image, fset=setImage, notify=imageChanged)

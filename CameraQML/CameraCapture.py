import numpy as np
import threading
import cv2
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty, QMetaObject, Q_ARG, Qt
from PyQt5.QtGui import qRgb, QImage

gray_color_table = [qRgb(i, i, i) for i in range(256)]


class CameraCapture(QObject):
    started = pyqtSignal()
    imageReady = pyqtSignal()
    sourceChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(CameraCapture, self).__init__(parent)
        self._image = QImage()
        self._source = 0

        self.m_videoCapture = cv2.VideoCapture()
        self.m_busy = False

    @pyqtSlot()
    @pyqtSlot(int)
    def start(self, *args):
        if args:
            self.setSource(args[0])

        self.m_videoCapture.release()
        self.m_videoCapture = cv2.VideoCapture(self._source)

        if self.m_videoCapture.isOpened():
            self.m_busy = True
            threading.Thread(target=self.process_image, args=()).start()
            self.started.emit()

    @pyqtSlot()
    def stop(self):
        self.m_busy = False

    @pyqtSlot(np.ndarray)
    def process_image(self):
        while self.m_busy:
            ret, frame = self.m_videoCapture.read()
            image = CameraCapture.ToQImage(frame)
            QMetaObject.invokeMethod(self, "setImage", Qt.QueuedConnection, Q_ARG(QImage, image))

    @staticmethod
    def ToQImage(im):
        if im is None:
            return QImage()

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy()

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    w, h, _ = im.shape
                    rgb_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                    flip_image = cv2.flip(rgb_image, 1)
                    qim = QImage(flip_image.data, h, w, QImage.Format_RGB888)
                    return qim.copy()

        return QImage()

    def image(self):
        return self._image

    @pyqtSlot(QImage)
    def setImage(self, image):
        if self._image == image:
            return

        self._image = image
        self.imageReady.emit()

    def source(self):
        return self._source

    def setSource(self, source):
        if self._source == source:
            return

        self._source = source
        self.sourceChanged.emit()

    image = pyqtProperty(QImage, fget=image, notify=imageReady)
    source = pyqtProperty(int, fget=source, fset=setSource, notify=sourceChanged)
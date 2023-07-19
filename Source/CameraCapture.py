import numpy as np
import threading
import cv2
import socket
import select
import struct
import pickle
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty, QMetaObject, Q_ARG, Qt
from PyQt5.QtGui import qRgb, QImage

gray_color_table = [qRgb(i, i, i) for i in range(256)]


class CameraCapture(QObject):
    started = pyqtSignal()
    imageReady = pyqtSignal()
    sourceChanged = pyqtSignal()
    sourceTypeChanged = pyqtSignal()
    streamAvailable = pyqtSignal()
    streamNotAvailable = pyqtSignal()

    def __init__(self, parent=None):
        super(CameraCapture, self).__init__(parent)
        self._image = QImage()
        self._camServerIP = '127.0.0.1'
        self._source = 0
        self._sourceType = "opencv"

        self.m_videoCapture = cv2.VideoCapture()
        self.m_busy = False
        print("Camera object created.")

    @pyqtSlot()
    def start(self):

        if self._sourceType == "socket":
            self.m_busy = True
            threading.Thread(target=self.socketFrameCapture, args=()).start()
            self.started.emit()

        elif self._sourceType == "opencv":
            self.m_videoCapture.release()
            self.m_videoCapture = cv2.VideoCapture(self._source)

            if self.m_videoCapture.isOpened():
                self.m_busy = True
                threading.Thread(target=self.opencvFrameCapture, args=()).start()
                self.started.emit()

        elif self._sourceType == "gstreamer":
            self.m_videoCapture.release()
            self.m_videoCapture = cv2.VideoCapture(self._source, cv2.CAP_GSTREAMER)

            if self.m_videoCapture.isOpened():
                self.m_busy = True
                threading.Thread(target=self.opencvFrameCapture, args=()).start()
                self.started.emit()

        else:
            print("No sourceType defined for camera object")

    @pyqtSlot()
    def stop(self):
        self.m_busy = False

    @pyqtSlot(np.ndarray)
    def opencvFrameCapture(self):
        self.streamAvailable.emit()
        while self.m_busy:
            try:
                ret, frame = self.m_videoCapture.read()

                # If no frame received, display a black screen
                if not ret:
                    frame = 0 * frame

                image = CameraCapture.ToQImage(frame)
                QMetaObject.invokeMethod(self, "setImage", Qt.QueuedConnection, Q_ARG(QImage, image))
            except:
                break

        self.m_videoCapture.release()
        self.streamNotAvailable.emit()

    @pyqtSlot()
    def socketFrameCapture(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self._camServerIP, self._source))
        server_socket.listen(5)

        while self.m_busy:
            print('Waiting for a new camera connection...')

            self.streamNotAvailable.emit()

            client_socket = socket.socket()
            while self.m_busy:
                ready_to_read, _, _ = select.select([server_socket], [], [], 0)
                if server_socket in ready_to_read:
                    client_socket, addr = server_socket.accept()
                    print('Connection from:', addr)
                    break

            self.streamAvailable.emit()

            data = b''
            payload_size = struct.calcsize('Q')

            while self.m_busy:
                while len(data) < payload_size:
                    packet = client_socket.recv(4 * 1024)  # Adjust the buffer size as needed
                    if not packet:
                        break
                    data += packet

                if not packet:
                    break

                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack('Q', packed_msg_size)[0]

                while len(data) < msg_size:
                    data += client_socket.recv(4 * 1024)  # Adjust the buffer size as needed

                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)

                image = CameraCapture.ToQImage(frame)
                QMetaObject.invokeMethod(self, "setImage", Qt.QueuedConnection, Q_ARG(QImage, image))

        # Release resources
        client_socket.close()
        server_socket.close()

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

    def sourceType(self):
        return self._sourceType

    def setSourceType(self, source_type):
        if self._sourceType == source_type:
            return

        self._sourceType = source_type
        self.sourceTypeChanged.emit()

    image = pyqtProperty(QImage, fget=image, notify=imageReady)
    source = pyqtProperty(int, fget=source, fset=setSource, notify=sourceChanged)
    sourceType = pyqtProperty(str, fget=sourceType, fset=setSourceType, notify=sourceTypeChanged)

import sys
import Assets.QRC.Resources
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from BackendController import BackendController
from CameraCapture import CameraCapture


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backendController = BackendController()
    engine.rootContext().setContextProperty("backendController", backendController)

    cameraCapture = CameraCapture()
    engine.rootContext().setContextProperty("cameraCapture", cameraCapture)

    engine.quit.connect(app.quit)
    engine.load('./main.qml')

    sys.exit(app.exec())

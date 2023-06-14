import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from BackendController import BackendController
from CameraQML.CameraCapture import CameraCapture
from CameraQML.CameraView import CameraView
import Assets.QRC.Resources


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRegisterType(CameraCapture, "CameraQML", 1, 0, "CameraCapture")
    qmlRegisterType(CameraView, "CameraQML", 1, 0, "CameraView")

    backendController = BackendController()
    engine.rootContext().setContextProperty("backendController", backendController)

    # cameraCapture = CameraCapture()
    # engine.rootContext().setContextProperty("cameraCapture", cameraCapture)

    engine.quit.connect(app.quit)
    engine.load('./main.qml')

    sys.exit(app.exec())

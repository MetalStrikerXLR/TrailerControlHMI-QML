from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot, QTimer


class BackendController(QObject):
    dataReceived = pyqtSignal(str)
    resetComplete = pyqtSignal()

    frontLockStateChanged = pyqtSignal()
    backLockStateChanged = pyqtSignal()
    steerLockStateChanged = pyqtSignal()

    dumpBagsStateChanged = pyqtSignal()
    compressorStateChanged = pyqtSignal()
    lightStateChanged = pyqtSignal()

    relay1StateChanged = pyqtSignal()
    relay2StateChanged = pyqtSignal()
    relay3StateChanged = pyqtSignal()
    relay4StateChanged = pyqtSignal()
    relay5StateChanged = pyqtSignal()
    relay6StateChanged = pyqtSignal()

    frontPressChanged = pyqtSignal()
    tankPressChanged = pyqtSignal()
    rearPressChanged = pyqtSignal()

    brakePercentChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_frontLockState = False
        self.m_backLockState = False
        self.m_steerLockState = False

        self.m_dumpBagsState = False
        self.m_compressorState = False
        self.lightState = False

        self.m_relay1State = False
        self.m_relay2State = False
        self.m_relay3State = False
        self.m_relay4State = False
        self.m_relay5State = False
        self.m_relay6State = False

        self.m_frontPressure = 0
        self.m_tankPressure = 0
        self.m_rearPressure = 0
        self.m_brakePercent = 0

        print("Init complete")

    @pyqtSlot()
    def resetUI(self):
        print("Arduino reset triggered. Resetting UI as well")
        self.resetComplete.emit()

    # ---------------------------------------- QML Exposed Properties ---------------------------------------- #

    @pyqtProperty(float, notify=frontLockStateChanged)
    def frontLockState(self):
        return self.m_frontLockState

    @frontLockState.setter
    def frontLockState(self, state):
        self.m_frontLockState = state
        self.frontLockStateChanged.emit()

    @pyqtProperty(float, notify=backLockStateChanged)
    def backLockState(self):
        return self.m_backLockState

    @backLockState.setter
    def backLockState(self, state):
        self.m_backLockState = state
        self.backLockStateChanged.emit()

    @pyqtProperty(float, notify=steerLockStateChanged)
    def steerLockState(self):
        return self.m_steerLockState

    @steerLockState.setter
    def steerLockState(self, state):
        self.m_steerLockState = state
        self.steerLockStateChanged.emit()

    @pyqtProperty(float, notify=dumpBagsStateChanged)
    def dumpBagsState(self):
        return self.m_dumpBagsState

    @dumpBagsState.setter
    def dumpBagsState(self, state):
        self.m_dumpBagsState = state
        self.dumpBagsStateChanged.emit()

    @pyqtProperty(float, notify=compressorStateChanged)
    def compressorState(self):
        return self.m_compressorState

    @compressorState.setter
    def compressorState(self, state):
        self.m_compressorState = state
        self.compressorStateChanged.emit()

    @pyqtProperty(float, notify=lightStateChanged)
    def lightState(self):
        return self.m_lightState

    @lightState.setter
    def lightState(self, state):
        self.m_lightState = state
        self.lightStateChanged.emit()

    @pyqtProperty(float, notify=relay1StateChanged)
    def relay1State(self):
        return self.m_relay1State

    @relay1State.setter
    def relay1State(self, state):
        self.m_relay1State = state
        self.relay1StateChanged.emit()

    @pyqtProperty(int, notify=relay2StateChanged)
    def relay2State(self):
        return self.m_relay2State

    @relay2State.setter
    def relay2State(self, state):
        self.m_relay2State = state
        self.relay2StateChanged.emit()

    @pyqtProperty(int, notify=relay3StateChanged)
    def relay3State(self):
        return self.m_relay3State

    @relay3State.setter
    def relay3State(self, state):
        self.m_relay3State = state
        self.relay3StateChanged.emit()

    @pyqtProperty(int, notify=relay4StateChanged)
    def relay4State(self):
        return self.m_relay4State

    @relay4State.setter
    def relay4State(self, state):
        self.m_relay4State = state
        self.relay4StateChanged.emit()

    @pyqtProperty(int, notify=relay5StateChanged)
    def relay5State(self):
        return self.m_relay5State

    @relay5State.setter
    def relay5State(self, state):
        self.m_relay5State = state
        self.relay5StateChanged.emit()

    @pyqtProperty(int, notify=relay6StateChanged)
    def relay6State(self):
        return self.m_relay6State

    @relay6State.setter
    def relay6State(self, state):
        self.m_relay6State = state
        self.relay6StateChanged.emit()

    @pyqtProperty(int, notify=frontPressChanged)
    def frontPressure(self):
        return self.m_frontPress

    @frontPressure.setter
    def frontPressure(self, pressure):
        self.m_frontPressure = pressure
        self.frontPressChanged.emit()

    @pyqtProperty(int, notify=tankPressChanged)
    def tankPressure(self):
        return self.m_tankPressure

    @tankPressure.setter
    def tankPressure(self, pressure):
        self.m_tankPressure = pressure
        self.tankPressChanged.emit()

    @pyqtProperty(int, notify=rearPressChanged)
    def rearPressure(self):
        return self.m_rearPressure

    @rearPressure.setter
    def rearPressure(self, pressure):
        self.m_rearPressure = pressure
        self.rearPressChanged.emit()

    @pyqtProperty(int, notify=brakePercentChanged)
    def brakePercent(self):
        return self.m_brakePercent

    @brakePercent.setter
    def brakePercent(self, percent):
        self.m_brakePercent = percent
        self.brakePercentChanged.emit()
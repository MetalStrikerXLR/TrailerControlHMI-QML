import paho.mqtt.client as mqtt
from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot


class BackendController(QObject):

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
        self.m_lightState = False

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

        print("Setting Up MQTT client")

        self.m_mqttServerIp = "test.mosquitto.org"
        self.m_mqttServerPort = 1883

        self.m_ctrlTopic = "trailer/ctrl/"
        self.m_monTopic = "trailer/mon/"

        self.m_mqttClient = mqtt.Client()
        self.m_mqttClient.on_connect = self.on_connect
        self.m_mqttClient.on_message = self.on_message

        self.m_mqttClient.connect(self.m_mqttServerIp, self.m_mqttServerPort, 60)
        self.m_mqttClient.loop_start()

        print("Backend init complete")

    # @staticmethod
    def on_connect(self, client, userdata, flags, rc):

        if rc == 0:
            print("Connected to MQTT server.")

            # Get Relay states
            client.subscribe(self.m_monTopic + "relay1")
            client.subscribe(self.m_monTopic + "relay2")
            client.subscribe(self.m_monTopic + "relay3")
            client.subscribe(self.m_monTopic + "relay4")
            client.subscribe(self.m_monTopic + "relay5")
            client.subscribe(self.m_monTopic + "relay6")

            # Get Sensor values
            client.subscribe(self.m_monTopic + "frontPressure")
            client.subscribe(self.m_monTopic + "tankPressure")
            client.subscribe(self.m_monTopic + "rearPressure")
            client.subscribe(self.m_monTopic + "brakePercent")

            # Get Button trigger confirmations
            client.subscribe(self.m_monTopic + "frontLockState")
            client.subscribe(self.m_monTopic + "backLockState")
            client.subscribe(self.m_monTopic + "steerLockState")
            client.subscribe(self.m_monTopic + "dumpBagsState")
            client.subscribe(self.m_monTopic + "compressorState")
            client.subscribe(self.m_monTopic + "lightState")

        else:
            print("Connection to MQTT server failed with code:", rc)

    # @staticmethod
    def on_message(self, client, userdata, msg):

        data = msg.payload.decode('UTF-8')

        if 'relay1' in msg.topic:
            self.relay1State = int(data)

        if 'relay2' in msg.topic:
            self.relay2State = int(data)

        if 'relay3' in msg.topic:
            self.relay3State = int(data)

        if 'relay4' in msg.topic:
            self.relay4State = int(data)

        if 'relay5' in msg.topic:
            self.relay5State = int(data)

        if 'relay6' in msg.topic:
            self.relay6State = int(data)

        if 'frontPressure' in msg.topic:
            self.frontPressure = int(float(data))

        if 'tankPressure' in msg.topic:
            self.tankPressure = int(float(data))

        if 'rearPressure' in msg.topic:
            self.rearPressure = int(float(data))

        if 'brakePercent' in msg.topic:
            self.brakePercent = int(float(data))

        if 'frontLockState' in msg.topic:
            self.frontLockState = int(data)

        if 'backLockState' in msg.topic:
            self.backLockState = int(data)

        if 'steerLockState' in msg.topic:
            self.steerLockState = int(data)

        if 'dumpBagsState' in msg.topic:
            self.dumpBagsState = int(data)

        if 'compressorState' in msg.topic:
            self.compressorState = int(data)

        if 'lightState' in msg.topic:
            self.lightState = int(data)

    @pyqtSlot(bool)
    def frontLockTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "frontLockState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def backLockTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "backLockState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def steerLockTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "steerLockState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def dumpBagsTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "dumpBagsState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def compressorTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "compressorState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def lightsTriggered(self, state):
        self.m_mqttClient.publish(self.m_ctrlTopic + "lightState", payload=state, qos=0, retain=False)

    @pyqtSlot(bool)
    def cameraTriggered(self, state):
        pass

    @pyqtSlot()
    def brakeIncPressed(self):
        self.m_mqttClient.publish(self.m_ctrlTopic + "brakeInc", payload="1", qos=0, retain=False)

    @pyqtSlot()
    def brakeIncReleased(self):
        pass

    @pyqtSlot()
    def brakeDecPressed(self):
        self.m_mqttClient.publish(self.m_ctrlTopic + "brakeDec", payload="1", qos=0, retain=False)

    @pyqtSlot()
    def brakeDecReleased(self):
        pass

    @pyqtSlot()
    def brakeTriggered(self):
        self.m_mqttClient.publish(self.m_ctrlTopic + "brakeState", payload="1", qos=0, retain=False)

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
        return self.m_frontPressure

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
import QtQuick 2.12
import QtQuick.Controls 2.12
import CameraQML 1.0
import "../Components"

Item {
    id: controlPageRoot
    property string objectName: "ControlPage"

    property alias camCapture: camCapture

    property int glowPixel: 17
    property int glowPixelRelay: 9

    Image {
        id: background
        anchors.fill: parent
        source: "qrc:/Assets/Background/Background.png"
    }

    Image {
        id: trailerInfoView
        width: respWidth(1042)
        height: respHeight(148)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(341)
        anchors.leftMargin: respWidth(309)

        source: "qrc:/Assets/Background/TrailerView.png"
    }

    // --------------------- Camera ----------------------------//

    Popup {
        id: cameraPopUp
        x: respWidth(280)
        y: respHeight(30)
        width: respWidth(1080)
        height: respHeight(600)
        modal: false
        focus: false
        visible: false
        opacity: 0
        closePolicy: Popup.CloseOnEscape
        clip: true

        background: Rectangle {
            color: "black"
            border.color: "gray"
            border.width: respAvg(3)
            radius: respAvg(30)
            clip: true

            Label {
                id: noPreviewLabel
                anchors.centerIn: parent
                text: "No Preview"
                color: "white"
                font.pixelSize: respAvg(60)
                visible: true
            }

            CameraView  {
                id: camViewer
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                width: respWidth(1040)
                height: respHeight(560)
                image: camCapture.image
                visible: false
            }

            CameraCapture{
                id: camCapture
                sourceType: "socket"
                source: 8485
                onStreamAvailable: camViewer.visible = true
                onStreamNotAvailable: camViewer.visible = false
                Component.onCompleted: camCapture.start()
            }
        }

        Behavior on opacity {
            NumberAnimation {
                duration: 300
            }
        }

        function open() {
            visible = true
            cameraPopUp.opacity = 1
        }

        function close() {
            cameraPopUp.opacity = 0
        }

        onOpacityChanged: {
            if (opacity === 0) {
                visible = false
            }
        }
    }

    // --------------------- Relays ----------------------------//

    ToggleableButton {
        id: relay1
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(549) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay1State
    }

    ToggleableButton {
        id: relay2
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(655) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay2State
    }

    ToggleableButton {
        id: relay3
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(761) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay3State
    }

    ToggleableButton {
        id: relay4
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(1010) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay4State
    }

    ToggleableButton {
        id: relay5
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(1116) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay5State
    }

    ToggleableButton {
        id: relay6
        width: respWidth(65) + respWidth(glowPixelRelay * 2)
        height: respHeight(65) + respWidth(glowPixelRelay * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(292) - respWidth(glowPixelRelay)
        anchors.leftMargin: respWidth(1222) - respWidth(glowPixelRelay)

        iconOffState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOffPressedState: "qrc:/Assets/Indicators/RelayIndicator_Red.png"
        iconOnState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"
        iconOnPressedState: "qrc:/Assets/Indicators/RelayIndicator_Green.png"

        isOn: backendController.relay6State
    }

    // --------------------- Pressure ----------------------------//

    Rectangle {
        id: frontPressure
        width: respWidth(187)
        height: respHeight(121)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(489)
        anchors.leftMargin: respWidth(394)
        color: "transparent"

        property int value: backendController.frontPressure

        Label {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(44)
            font.family: "Inter"
            text: frontPressure.value + " PSI"
        }

        Label {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(26)
            font.family: "Inter"
            text: "Front"
        }
    }

    Rectangle {
        id: tankPressure
        width: respWidth(187)
        height: respHeight(121)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(489)
        anchors.leftMargin: respWidth(692)
        color: "transparent"

        property int value: backendController.tankPressure

        Label {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(44)
            font.family: "Inter"
            text: tankPressure.value + " PSI"
        }

        Label {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(26)
            font.family: "Inter"
            text: "Tank"
        }
    }

    Rectangle {
        id: rearPressure
        width: respWidth(187)
        height: respHeight(121)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(489)
        anchors.leftMargin: respWidth(989)
        color: "transparent"

        property int value: backendController.rearPressure

        Label {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(44)
            font.family: "Inter"
            text: rearPressure.value + " PSI"
        }

        Label {
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#31DB16"
            font.pixelSize: respAvg(26)
            font.family: "Inter"
            text: "Rear"
        }
    }

    // --------------------- Buttons ----------------------------//

    ToggleableButton {
        id: frontLockBtn
        width: respWidth(205) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(59) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(43) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/FLockBtn_Green.png"
        iconOffPressedState: "qrc:/Assets/Buttons/FLockBtn_Green.png"
        iconOnState: "qrc:/Assets/Buttons/FLockBtn_Red.png"
        iconOnPressedState: "qrc:/Assets/Buttons/FLockBtn_Red.png"

        isOn: backendController.frontLockState

        onClicked: {
            backendController.frontLockTriggered(!frontLockBtn.isOn)
        }
    }

    ToggleableButton {
        id: backLockBtn
        width: respWidth(205) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(192) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(43) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/BLockBtn_Green.png"
        iconOffPressedState: "qrc:/Assets/Buttons/BLockBtn_Green.png"
        iconOnState: "qrc:/Assets/Buttons/BLockBtn_Red.png"
        iconOnPressedState: "qrc:/Assets/Buttons/BLockBtn_Red.png"

        isOn: backendController.backLockState

        onClicked: {
            backendController.backLockTriggered(!backLockBtn.isOn)
        }
    }

    ToggleableButton {
        id: steerLockBtn
        width: respWidth(205) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(325) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(43) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/SLockBtn_Green.png"
        iconOffPressedState: "qrc:/Assets/Buttons/SLockBtn_Green.png"
        iconOnState: "qrc:/Assets/Buttons/SLockBtn_Red.png"
        iconOnPressedState: "qrc:/Assets/Buttons/SLockBtn_Red.png"

        isOn: backendController.steerLockState

        onClicked: {
            backendController.steerLockTriggered(!steerLockBtn.isOn)
        }
    }

    ToggleableButton {
        id: dumpBagsBtn
        width: respWidth(205) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(528) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(43) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/DumpBagsBtn_Red.png"
        iconOffPressedState: "qrc:/Assets/Buttons/DumpBagsBtn_Red.png"
        iconOnState: "qrc:/Assets/Buttons/DumpBagsBtn_Green.png"
        iconOnPressedState: "qrc:/Assets/Buttons/DumpBagsBtn_Green.png"

        isOn: backendController.dumpBagsState

        onClicked: {
            backendController.dumpBagsTriggered(!dumpBagsBtn.isOn)
        }
    }

    ToggleableButton {
        id: compressorBtn
        width: respWidth(205) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(665) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(43) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/CompBtn_Red.png"
        iconOffPressedState: "qrc:/Assets/Buttons/CompBtn_Red.png"
        iconOnState: "qrc:/Assets/Buttons/CompBtn_Green.png"
        iconOnPressedState: "qrc:/Assets/Buttons/CompBtn_Green.png"

        isOn: backendController.compressorState

        onClicked: {
            backendController.compressorTriggered(!compressorBtn.isOn)
        }
    }

    ToggleableButton {
        id: lightsBtn
        width: respWidth(190) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(665) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(301) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/LightsBtn_Green.png"
        iconOffPressedState: "qrc:/Assets/Buttons/LightsBtn_Green.png"
        iconOnState: "qrc:/Assets/Buttons/LightsBtn_Red.png"
        iconOnPressedState: "qrc:/Assets/Buttons/LightsBtn_Red.png"

        isOn: backendController.lightState

        onClicked: {
            backendController.lightsTriggered(!lightsBtn.isOn)
        }
    }

    PressableButton {
        id: brakeIncBtn
        width: respWidth(100) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(663) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(539) - respWidth(glowPixel)

        iconSrc: "qrc:/Assets/Buttons/BrakeIncBtn_Green.png"
        iconPressedState: "qrc:/Assets/Buttons/BrakeIncBtn_Red.png"

        onPressed: {
            backendController.brakeIncPressed()
        }

        onReleased: {
            backendController.brakeIncReleased()
        }
    }

    PressableButton {
        id: brakeBtn
        width: respWidth(319) + respWidth(glowPixel * 2)
        height: respHeight(89) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(668) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(670) - respWidth(glowPixel)

        iconSrc: "qrc:/Assets/Buttons/BrakeBtn_Green.png"
        iconPressedState: "qrc:/Assets/Buttons/BrakeBtn_Red.png"

        property int brakePercent: backendController.brakePercent

        Label {
            anchors.centerIn: parent
            color: "#FFFFFF"
            font.pixelSize: respAvg(22)
            font.family: "Inter"
            text: "Brake " + brakeBtn.brakePercent + "%"
        }

        onPressed: {
            backendController.brakeTriggered()
        }
    }

    PressableButton {
        id: brakeDecBtn
        width: respWidth(100) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(663) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(1010) - respWidth(glowPixel)

        iconSrc: "qrc:/Assets/Buttons/BrakeDecBtn_Green.png"
        iconPressedState: "qrc:/Assets/Buttons/BrakeDecBtn_Red.png"

        onPressed: {
            backendController.brakeDecPressed()
        }

        onReleased: {
            backendController.brakeDecReleased()
        }
    }

    ToggleableButton {
        id: cameraBtn
        width: respWidth(190) + respWidth(glowPixel * 2)
        height: respHeight(100) + respWidth(glowPixel * 2)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(663) - respWidth(glowPixel)
        anchors.leftMargin: respWidth(1156) - respWidth(glowPixel)

        iconOffState: "qrc:/Assets/Buttons/CameraBtn_Green.png"
        iconOffPressedState: "qrc:/Assets/Buttons/CameraBtn_Green.png"
        iconOnState: "qrc:/Assets/Buttons/CameraBtn_Red.png"
        iconOnPressedState: "qrc:/Assets/Buttons/CameraBtn_Red.png"

        onClicked: {
            cameraBtn.isOn = !cameraBtn.isOn
            backendController.cameraTriggered(cameraBtn.isOn)

            if(cameraBtn.isOn == true) {
                cameraPopUp.open()
            }
            else {
                cameraPopUp.close()
            }
        }
    }

    Connections {
        //        target: outputcontroller

        //        function onResetComplete() {
        //            frontLockBtn.isOn = false
        //        }
    }

    // --------------------- Test Sliders ----------------------------//

    Row {
        visible: false
        id: testPanel
        spacing: respWidth(20)
        width: respWidth(1042)
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.topMargin: respHeight(30)
        anchors.leftMargin: respWidth(309)

        Column {
            width: parent.width/2
            spacing: respHeight(20)

            Slider {
                id: sliderA
                width: parent.width

                onValueChanged: {
                    frontPressure.value = Math.round(sliderA.value * 100)
                }
            }

            Slider {
                id: sliderB
                width: parent.width

                onValueChanged: {
                    tankPressure.value = Math.round(sliderB.value * 100)
                }
            }

            Slider {
                id: sliderC
                width: parent.width

                onValueChanged: {
                    rearPressure.value = Math.round(sliderC.value * 100)
                }
            }

            Slider {
                id: sliderD
                width: parent.width
                onValueChanged: {
                    brakeBtn.brakePercent = Math.round(sliderD.value * 100)
                }
            }
        }

        Column {
            spacing:respHeight(10)
            Button {
                text: "Relay 1"
                onClicked: {
                    relay1.isOn = !relay1.isOn
                }
            }

            Button {
                text: "Relay 2"
                onClicked: {
                    relay2.isOn = !relay2.isOn
                }
            }

            Button {
                text: "Relay 3"
                onClicked: {
                    relay3.isOn = !relay3.isOn
                }
            }
        }

        Column {
            spacing:respHeight(10)

            Button {
                text: "Relay 4"
                onClicked: {
                    relay4.isOn = !relay4.isOn
                }
            }

            Button {
                text: "Relay 5"
                onClicked: {
                    relay5.isOn = !relay5.isOn
                }
            }

            Button {
                text: "Relay 6"
                onClicked: {
                    relay6.isOn = !relay6.isOn
                }
            }
        }
    }
}

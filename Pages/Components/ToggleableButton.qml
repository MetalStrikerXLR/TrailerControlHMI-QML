import QtQuick 2.12
import QtQuick.Controls 2.12

MouseArea {
    id: tabBtn
    width: 352
    height: 130

    property bool isOn: false

    property string iconOffState: ""
    property string iconOnState: ""
    property string iconOnPressedState: ""
    property string iconOffPressedState: ""

    Image {
        id: icn
        width: tabBtn.width
        height: tabBtn.height
    }

    states: [
        State {
            name: "offState"
            PropertyChanges { target: icn; source: iconOffState}
        },
        State {
            name: "offPressedState"
            PropertyChanges { target: icn; source: iconOffPressedState}
        },
        State {
            name: "onState"
            PropertyChanges { target: icn; source: iconOnState}
        },
        State {
            name: "onPressedState"
            PropertyChanges { target: icn; source: iconOnPressedState}
        }
    ]
    state: pressed ? (isOn ? "onPressedState" : "offPressedState")
                   : (isOn ? "onState" : "offState")
}

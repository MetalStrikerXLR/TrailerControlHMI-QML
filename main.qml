import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import "./Pages/ControlPage"

Window {
    id: appRoot
    width: 1375
    height: 825
    visible: true
    title: qsTr("Trailer Control")

    property int baseWidth: 1375
    property int baseHeight: 825
    property real baseAvg: Math.hypot(baseWidth, baseHeight)

    function respWidth(w) {
        return appRoot.width * (w/baseWidth);
    }

    function respHeight(h) {
        return appRoot.height * (h/baseHeight);
    }

    function respAvg(a) {
        var assetAvg = Math.hypot(a, a);
        return Math.round(Math.hypot(appRoot.height,appRoot.width) * (assetAvg / baseAvg));
    }

    ControlPage {
        id: controlPage
        anchors.fill: parent
        visible: true
    }

    onClosing: {
        console.log("Closing")
        controlPage.camCapture.stop()
    }
}

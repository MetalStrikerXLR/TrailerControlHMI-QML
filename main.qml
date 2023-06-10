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
    property real baseAvg: 1603.51

    function respWidth(w) {
        return appRoot.width * (w/baseWidth);
    }

    function respHeight(h) {
        return appRoot.height * (h/baseHeight);
    }

    function respAvg(a) {
        var assetAvg = Math.sqrt(Math.pow(a, 2) + Math.pow(a, 2));
        return Math.round(Math.sqrt(Math.pow(appRoot.height, 2) + Math.pow(appRoot.width, 2)) * (assetAvg / baseAvg));
    }

    ControlPage {
        id: controlPage
        anchors.fill: parent
        visible: true
    }
}

Tested on RP3 3B+ - Raspbian OS Lite (Bullseye 32-bit)


Step1). Install build tools and Update pip and setuptools:
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install pip
- python3 -m pip install --upgrade pip
- python3 -m pip install --upgrade setuptools
- sudo apt-get install qt5-qmake
- sudo apt-get install qml-module-qtquick-controls qml-module-qtquick-shapes qml-module-qtquick-controls2
- sudo apt-get install python3-pyqt5.qtquick python3-pyqt5.qtwebkit python3-pyqt5.qtmultimedia
- sudo apt-get install python3-paho-mqtt
- sudo apt-get install python3-opencv

Step2). Enable Mosquitto server
- sudo apt install mosquitto mosquitto-clients
- sudo systemctl enable mosquitto.service
- sudo nano /etc/mosquitto/mosquitto.conf
- 'listener 1883' in mosquitto.conf
- 'allow_anonymous true' in mosquitto.conf
- sudo systemctl restart mosquitto

Step3). Execute GUI on Rpi locally (cannot be deployed using SSH):
- export QT_QPA_EGLFS_HIDECURSOR=1 (hide cursor)
- python3 main.py --platform eglfs

Note1: Enable OpenGL for QML app by going to raspi-config (Enabled by default on Raspberry Pi 4)

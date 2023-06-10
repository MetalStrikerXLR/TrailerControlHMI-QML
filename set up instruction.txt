Reference: https://forums.raspberrypi.com/viewtopic.php?t=330264


Step1). Install dbuild toolsand Update pip and setuptools:
- sudo apt-get install pip
- python3 -m pip install --upgrade pip
- python3 -m pip install --upgrade setuptools
- pip3 install pyinstaller
- sudo apt-get install qtbase5-dev
- sudo apt install libqt5opengl5-dev
- sudo apt-get install qtdeclarative5-dev
- sudo apt-get install qml-module-qtquick-controls qml-module-qtquick-shapes qml-module-qtquick-controls2
- sudo apt-get install libqt5serialport5-dev
- sudo apt-get install python3-pyqt5.qtquick
- sudo apt-get install python3-pyqt5.qtserialport


Step2). Install PyQt5 (will take alot of time ~2-3h):
- python3 -m pip install pyqt5 --config-settings --confirm-license= --verbose


Step3). Install display server:
- sudo apt-get install xorg
- sudo nano /etc/X11/Xwrapper.config
- allowed_users=console -> allowed_users=anybody
- save changes


Step4). Upload firmware code to Arduino Mega


Step5). Upload code to Raspberry Pi:


Step6). Go to directory where code is placed and Compile Binary:
- pyinstaller --onefile main.py && cp ./dist/main ./ && mv main BoatControllerApp && rm -rf dist && rm -rf build && rm -rf main.spec

The exe file will be created by name : BoatControllerApp


Step7). Test Serial UART:
- minicom -b 115200 -D /dev/ttyUSB0 - (IF using USB)
- minicom -b 115200 -D /dev/ttyAMA0 - (IF using TTL Shifter)
- You will start to get data if connections are good and arduino in powered on


Step8). Run Application using Xorg:
- export DISPLAY=:0
- sudo startx <absolute path to BoatControllerApp> -geometry 1920x1080+0+0


Step8.5). If above step does not work then:
- export QT_QPA_EGLFS_HIDECURSOR=1 (hide cursor)
- python3 main.py --platform eglfs (not using SSH)


Note1: Enable OpenGL for QML app by going to raspi-config (Enabled by default on Raspberry Pi 4)

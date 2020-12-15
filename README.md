# Q-01P

![Q-01P](https://raw.githubusercontent.com/watai/Q-01P/images/q-01p.jpg)

## Technical Specifications
### Enclosure
- dimensions : 300 x 200 x 86 mm
- materials : acrylic panel, aluminium frame and wood board
### Controller
- Raspberry Pi 4 Model B / 4GB
### Sound Module
- stereo speaker unit : Dayton Audio DMA90-4
- DAC : Pi-DAC PRO (PCM5122)
- amplifier : Stereo Audio Amplifier 10W+10W (MAX9704)
### Power Requirements
- AC : 110-240V 50~60hz
universal built-in power supply
- DC : 12V4.3A switched-mode power supply (VS50E-12)

## Q-Audio
### Setup Q-Audio
```
$ sudo apt install -y python-pyaudio python3-pyaudio
$ pip3 install pyaudio wave
```
### Start Q-Audio
```
$ cd ~/Q-01/q-audio
$ python3 q-audio.py
# or
$ python3 q-audio-aplay.py
```
## Q-Encoder
### Setup Q-Encoder
```
$ sudo apt install i2c-tools
$ sudo i2cdetect -y 1
$ pip3 install smbus2 
```
### Start Q-Encoder
```
$ ~/Q-01/q-encoder
$ python3 q-encoder.py
```

## Q-Socket
### Setup Q-Socket
```
# websocket client
$ pip3 install websocket-client
# start websocket server
$ pip3 install git+https://github.com/Pithikos/python-websocket-servers
```
### Start Q-Socket
```
$ cd ~/Q-01/q-socket
# client
$ python3 ws-client.py
# server
$ python3 ws-server.py
```

## AirPlay Server
### Start AirPlay Server
```
$ sudo service shairport-sync start # start
$ sudo service shairport-sync stop # stop
$ sudo service shairport-sync restart # reboot
$ sudo service shairport-sync status # check status
```
### Setup Auto Startup
```
$ sudo systemctl enable shairport-sync.service
```

## Q-Viewer
### Dependencies
- Unity 2019.4.15f1
- Maps SDK for Unity v2.1.1
- Post Processing v3.0.1
- Multiplayer HLAPI v1.0.6
### Install the Maps SDK for Unity
Please follow the instruction [the installation guide](https://www.mapbox.com/install/unity/).

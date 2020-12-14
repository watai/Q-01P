# Q-01P

![Q-01P](https://raw.githubusercontent.com/watai/Q-01P/images/q-01p.jpg)

## Technical Specifications
### Enclosure
- dimensions : 300 x 200 x 86 mm
- materials : acrylic panel, aluminium Frame and wood board
### Controller
- Raspberry Pi 4 Model B / 4GB
### Sound Module
- stereo speaker unit : Dayton Audio DMA90-4
- DAC : Pi-DAC PRO (PCM5122)
- amplifier : Stereo Audio Amplifier 10W+10W (MAX9704)
### Power
- AC : 110-240V 50~60hz
universal built-in power supply
- DC : 12V4A internal power supply

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
# start
$ sudo service shairport-sync start
# stop
$ sudo service shairport-sync stop
# reboot
$ sudo service shairport-sync restart
# status
$ sudo service shairport-sync status
```
### Setup Auto Startup
```
$ sudo systemctl enable shairport-sync.service
```

## Q-Viewer

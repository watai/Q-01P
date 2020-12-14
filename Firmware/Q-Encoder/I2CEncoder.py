#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import smbus2
import RPi.GPIO as GPIO
from time import sleep
import i2cEncoderMiniLib

class I2CEncoder:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.INT_pin = 4
        GPIO.setup(self.INT_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        bus = smbus2.SMBus(1)

        self.enc = i2cEncoderMiniLib.i2cEncoderMiniLib(bus, 0x20)
        encconfig = (i2cEncoderMiniLib.WRAP_DISABLE | i2cEncoderMiniLib.DIRE_RIGHT | i2cEncoderMiniLib.IPUP_ENABLE | i2cEncoderMiniLib.RMOD_X1)
        self.enc.begin(encconfig)
        self.enc.writeCounter(0)
        self.enc.writeMax(100)
        self.enc.writeMin(0)
        self.enc.writeStep(1)    
        self.enc.writeDoublePushPeriod(50)
        # event handler
        self.enc.onChange = self.EncoderChange
        # self.enc.onIncrement = self.EncoderIncrement
        # self.enc.onDecrement = self.EncoderDecrement
        self.enc.onButtonPush = self.EncoderPush
        self.enc.onButtonRelease = self.EncoderRelease
        self.enc.onButtonDoublePush = self.EncoderDoublePush
        self.enc.onButtonLongPush = self.EncoderLongPush
        # self.enc.onMax = self.EncoderMax
        # self.enc.onMin = self.EncoderMin
        self.enc.autoconfigInterrupt()
        print('Board ID code: 0x%X' % (self.enc.readIDCode()))
        print('Board Version: 0x%X' % (self.enc.readVersion()))
        GPIO.add_event_detect(self.INT_pin, GPIO.FALLING, callback=self.EncoderINT, bouncetime=10)
    
    def EncoderChange(self):
        val = self.enc.readCounter32()
        print('Changed: %d' % (val))

    def EncoderIncrement(self):
        val = self.enc.readCounter32()
        print('Increment: %d' % (val))
        
    def EncoderDecrement(self):
        val = self.enc.readCounter32()
        print('Decrement: %d' % (val))

    def EncoderPush(self):
        print('Encoder Pushed!')
	
    def EncoderRelease(self):
        print('Encoder Released!')

    def EncoderDoublePush(self):
        print('Encoder Double Push!')

    def EncoderLongPush(self):
        print('Encoder Long Push!')

    def EncoderMax(self):
        print('Encoder max!')

    def EncoderMin(self):
        print('Encoder min!')
    
    def EncoderINT(self,channel):
        self.enc.updateStatus()

    def Close(self):
        GPIO.remove_event_detect(self.INT_pin)
        GPIO.cleanup()

if __name__ == "__main__":
    encoder = I2CEncoder()
    
    try:
        while True:
            pass       
    except KeyboardInterrupt:
        encoder.Close()
        quit()
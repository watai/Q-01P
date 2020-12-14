#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import I2CEncoder

if __name__ == "__main__":
    encoder = I2CEncoder.I2CEncoder()
    
    try:
        while True:
            pass       
    except KeyboardInterrupt:
        encoder.Close()
        quit()
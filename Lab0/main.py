# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyb 

#initalis pins timer and array
PC1 = pyb.Pin(pyb.Pin.cpu.C1, mode=pyb.Pin.OUT_PP)
adc = pyb.ADC(pyb.Pin.cpu.C0)
tim = pyb.Timer(6)
tim.init(freq=1000)   # trigger at 1kHz
volts = 2000*[0]
count = 0

PC1.low()

def timerCB(timer):
    global count
    volts[count] = adc.read()
    print("in timer callback: VAL ", volts[count])
    count += 1
    if count >= len(volts):
        tim.callback(None)
        PC1.low()

 
tim.callback(timerCB)    
PC1.high()      









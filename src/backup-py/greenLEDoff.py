#!/usr/bin/python
# -*- coding:utf-8 -*-

import wiringpi

#============  WiringPi Setup for switching on the external Power LED =====================
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,1);     #GPIO-Pin 18 becomes an output for LED status display
wiringpi.digitalWrite(18,0);   # LED on

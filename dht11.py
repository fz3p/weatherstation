#!/usr/bin/env python
# -*- coding: latin-1 -*-
# basé sur le script Adafruit et adapté pour Domoticz

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import Adafruit_DHT
from requests.auth import HTTPBasicAuth
import requests


# ############ Parametres #################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de Domoticz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

domoticz_ip = ''
domoticz_port = '8080'
user = ''
password = ''
domoticz_idx = ''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres du DHT
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# sensor est 11,22,ou 2302
# pin est le numero d la pin que vous avez cablée
# https://pinout.xyz/pinout/pin12_gpio18#

sensor = ''
pin = 18


# ############ Fin des parametres #################################


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# le fomat pour la temp hum est celui ci
# /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&
# svalue=TEMP;HUM;HUM_STAT


def maj_widget(val_url):
    requete = 'http://' + domoticz_ip + ':' + domoticz_port + val_url
    # print requete
    r = requests.get(requete, auth=HTTPBasicAuth(user, password))
    if r.status_code != 200:
        print("Erreur API Domoticz")


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    # l URL Domoticz pour le widget virtuel
    url = '/json.htm?type=command&param=udevice&idx=' + str(domoticz_idx)
    url += '&nvalue=0&svalue='
    url += str('{0:0.1f};{1:0.1f};2').format(temperature, humidity)
    print(url)
    maj_widget(url)

else:
    print('Probleme avec la lecture du DHT. Try again!')
    sys.exit(1)

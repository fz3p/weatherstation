#!/usr/bin/python
from bme280 import main
from requests.auth import HTTPBasicAuth
import requests
import sys
import Adafruit_DHT


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fonction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def maj_widget(val_url):
    requete = 'http://' + domoticz_ip + ':' + domoticz_port + val_url
    # print requete
    r = requests.get(requete, auth=HTTPBasicAuth(user, password))
    if r.status_code != 200:
        print("Erreur API Domoticz")


# 0=Normal
# 1=Comfortable
# 2=Dry
# 3=Wet
def humidity_status(val):
    if 0 <= val <= 75:
        humidity_status = 0
    elif 76 <= val <= 79:
        humidity_status = 1
    elif 80 <= val <= 94:
        humidity_status = 2
    elif 95 <= val <= 100:
        humidity_status = 3
    return humidity_status


# 0 = No info
# 1 = Sunny
# 2 = Partly cloudy
# 3 = Cloudy
# 4 = Rain
def barometer_forecast(val):
    if 990 <= val <= 1029:
        weather = 4
    elif 1030 <= val <= 1034:
        weather = 3
    elif 1035 <= val <= 1040:
        weather = 2
    elif 1041 <= val <= 1050:
        weather = 1
    else:
        weather = 0
    return weather


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de Domoticz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

domoticz_ip = ''
domoticz_port = '8080'
user = ''
password = ''
domoticz_idx = ''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# récuperation des informations des capteurs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# sensor est 11,22,ou 2302
# pin est le numero d la pin que vous avez cablée
# https://pinout.xyz/pinout/pin12_gpio18#
sensor = ''
pin = 18
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
hum_stat = humidity_status(humidity)

# préciser le DEVICE dans bme280.py ( sudo i2cdetect -y 1 )
value = main()
pressure = int(value[1])
bar_for = barometer_forecast(int(pressure))

if humidity is not None and temperature is not None and pressure is not None:

    # https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s#Temperature.2Fhumidity.2Fbarometer
    # modele url : /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&
    # svalue=TEMP;HUM;HUM_STAT;BAR;BAR_FOR
    # l URL Domoticz pour le widget virtuel

    url = '/json.htm?type=command&param=udevice&idx=' + str(domoticz_idx)
    url += '&nvalue=0&svalue='
    url += str('{0:0.1f};{1:0.1f};{2:0};{3:0.1f};{4:0}').format(temperature, humidity, hum_stat, pressure, bar_for)
    print(url)
    maj_widget(url)

else:
    print('Probleme avec la lecture du BME280. Try again!')
    sys.exit(1)

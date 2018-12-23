#!/usr/bin/python
from bme280 import main
from requests.auth import HTTPBasicAuth
import requests

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fonction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def maj_widget(val_url):
    requete = 'http://' + domoticz_ip + ':' + domoticz_port + val_url
    # print requete
    r = requests.get(requete, auth=HTTPBasicAuth(user, password))
    if r.status_code != 200:
        print("Erreur API Domoticz")


def barometer_forecast(val):
    if val >= 990 and val <= 1018:
        weather = 1
    elif val >= 1019 and val <= 1023:
        weather = 2
    elif val >= 1024 and val <= 1029:
        weather = 3
    elif val >= 1030 and val <= 1100: \
        weather = 4
    else:
        weather = 0
    return weather


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de Domoticz
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
domoticz_ip = ''
domoticz_port='8080'
user=''
password=''
domoticz_idx=''

# appelle de la fonction main de bmp280.py
value = main()
temperature = int(value[0])
pressure = int(value[1])
humidity = int(value[2])
bar_for = barometer_forecast(int(pressure))

if humidity is not None and temperature is not None and pressure is not None:

    # https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s#Temperature.2Fhumidity.2Fbarometer
    # modele url : /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&svalue=TEMP;HUM;HUM_STAT;BAR;BAR_FOR

    
    # l URL Domoticz pour le widget virtuel 
    url='/json.htm?type=command&param=udevice&idx='+str(domoticz_idx)
    url+='&nvalue=0&svalue='
    url+=str('{0:0.1f};{1:0.1f};{2:0.1f};{3:0}').format(temperature, humidity, pressure, bar_for)
    print(url)
    maj_widget(url)
 
else:
    print('Probleme avec la lecture du BMP280. Try again!')
    sys.exit(1)


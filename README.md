
# installation de python
`
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install
`


# installation de pip
`
sudo apt-get upgrade
sudo apt-get install python-pip
sudo pip install requests
`


# rendre executable
`chmod +x /home/user/script/dht11.py`


# automatisation 
`
sudo crontab -e
*/1 * * * * sudo /home/user/script/dht11.py
`
*http://fr.wikipedia.org/wiki/Crontab*# weatherstation*

# pin

## LED
GPIO7   =  +
GPIO30  =  - (+resistance 330)

## PHOTORESISTOR
config BCM faire conversion
GPIO16 	=  +
GPIO14  =  - 

## DHT11
config BCM faire conversion
GPIO1   =  alim
GPIO6 	=  grnd
GPIO12 	=  info

## BME280
GPIO2 	= alim
GPIO39  = grnd
GPIO3 	= SDA
GPIO5	= SCL





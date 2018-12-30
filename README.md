
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
*http://fr.wikipedia.org/wiki/Crontab*# weatherstation
Station météo avec un Raspberry 0 W

# coding: utf-8
#!/usr/bin/python

import RPi.GPIO as GPIO ## Import GPIO library
import time

LIGHT_PIN = 23    # photoresistor pin

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)


timeCount = 5*60 # envoi des données ttes les 5 minutes
old_time = time.time()
statut = True
compteur = 0

while True:
	new_time = time.time()
	totalTime = old_time + timeCount
	# si plus de 5 minutes d'écart, l'ancien temps devient le nouveau
	if new_time >= totalTime:
		old_time = new_time
		#envoi des données à domoticz
		#TODO
		# reinitialisation du compteur; 
		compteur = 0


    if GPIO.input(LIGHT_PIN) == 0:
        # s'incline gauche :
        # si déjà à gauche ne rien faire
        if statut == True:
			statut = False
			compteur = compteur + 1
			print(compteur)
    else : 
		statut = True
	time.sleep(0.1)

import RPi.GPIO as GPIO
from time import sleep     

# set the pin numbering to GPIO.BCM in order to use the GPIO numering, not the physical one
GPIO.setmode(GPIO.BCM)
# we set the GPIO pis as out to send signals through it
GPIO.setup(23,GPIO.OUT)   # pin 33 physical on Raspberry


def buzzer(time):
    # start sending signal to the buzzer, wait for a period, then stop the buzzer
    GPIO.output(23,GPIO.HIGH)
    sleep(time)
    GPIO.output(23,GPIO.LOW)
    

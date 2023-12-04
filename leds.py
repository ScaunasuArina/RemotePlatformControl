import RPi.GPIO as GPIO

# we set the pin numbering to GPIO.BCM in order to use the GPIO numering, not the physical one
GPIO.setmode(GPIO.BCM)

# we set the two ports for both LEDS
GPIO.setup(26, GPIO.OUT)   # left led (pin 37 physical)
GPIO.setup(20, GPIO.OUT)   # right led (pin 38 physical)


def leds_on():
    # set both pins to high in order to turn on the leds
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    print('Leds have been turned on')


def leds_off():    
    # we set both pins to low in order to turn off the leds
    GPIO.output(26, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    print('Leds have been turned off')
    

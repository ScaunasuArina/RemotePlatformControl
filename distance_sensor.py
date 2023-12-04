import RPi.GPIO as GPIO
import time

# set the pin numbering to GPIO.BCM in order to use the GPIO numering, not the physical one
GPIO.setmode(GPIO.BCM)

# define the pins used for this sensor
trig = 21       # the pin used to send the ultrasonic wave (pin 40 physical on Raspberry)
echo = 16       # the pin used to receive the ultrasonic wave (pin 36 physical on Raspberry)

# set the trigger pin as OUTPUT because we send signal through this pin
GPIO.setup(trig, GPIO.OUT)
# set the echo pin as INPUT because we receive data from this pin
GPIO.setup(echo, GPIO.IN)


def read_distance():
    distance = 0

    start = time.time()
    stop = time.time()
    
    # set the trig pin to high to send the ultrasonic wave
    GPIO.output(trig, GPIO.HIGH)
    # let the trig send ultrasonic wave for 1 microsecond
    time.sleep(0.00001)
    # set the trig pin to low to stop sending the ultrasonic wave
    GPIO.output(trig, GPIO.LOW)
    
    # modify the start time to be the last time until the echo pin becomes HIGH
    while GPIO.input(echo) == 0:
        start = time.time()

    # modify the stop time to be the last time until the echo pin becomes LOW
    while GPIO.input(echo) == 1:
        stop = time.time()

    duration = stop - start

    # calculate the distance with the formula d = (v*t)/2
    # where v = speed of sound
    distance = 34300/2 * duration

    # the reading can be erroneous, and we will print
    # the distance only if it is lower than the specified value
    if distance < 3400:
        # display the distance in console
        print ('Distance = %.2f cm.' % distance)
        return distance

import RPi.GPIO as GPIO
from time import sleep

# we set the pin numbering to GPIO.BCM in order to use the GPIO numering, not the physical one
GPIO.setmode(GPIO.BCM)

# Defining the parameters for both motors
# For each motor we use 2 pins to control the direction: front and back

PWMpinLF = 13     # for motor left Front
PWMpinLB = 19     # for motor left Back

PWMpinRF = 18     # for motor right Front
PWMpinRB = 12     # for motor right Back

# set the pins as output for both motors in order to control them with Raspberry
# left motor
GPIO.setup(PWMpinLF, GPIO.OUT)
GPIO.setup(PWMpinLB, GPIO.OUT)
# right motor
GPIO.setup(PWMpinRF, GPIO.OUT)
GPIO.setup(PWMpinRB, GPIO.OUT)

# set the PWM speed for the motors to 100
speed = 100

# set the PWM speed for left motor
PWMpinLF = GPIO.PWM(PWMpinLF, speed)    
PWMpinLB = GPIO.PWM(PWMpinLB, speed)
# set the PWM speed for right motor
PWMpinRF = GPIO.PWM(PWMpinRF, speed)    
PWMpinRB = GPIO.PWM(PWMpinRB, speed)

# set the duty cycle for all pins to 0
# left motor
PWMpinLF.start(0)
PWMpinLB.start(0)
# right motor
PWMpinRF.start(0)
PWMpinRB.start(0)


def turn_off():
    # this instructios are used to set the speed of the motors to 0 (Off)
    # left motor
    PWMpinLF.ChangeDutyCycle(0) 
    PWMpinLB.ChangeDutyCycle(0)

    # right motor
    PWMpinRF.ChangeDutyCycle(0) 
    PWMpinRB.ChangeDutyCycle(0)
 

def move_forward(delay):
    # the function for moving FORWARD for the defined period of time
    # left motor
    PWMpinLF.ChangeDutyCycle(50) 
    PWMpinLB.ChangeDutyCycle(0)

    # right motor
    PWMpinRF.ChangeDutyCycle(50) 
    PWMpinRB.ChangeDutyCycle(0)    
    # let the platform move forward for the defined time
    sleep(delay)
    # turn off the motors
    turn_off()
                

def move_backward(delay):
    # the function for moving BACKWARD for the defined period of time
    # left motor
    PWMpinLF.ChangeDutyCycle(0) 
    PWMpinLB.ChangeDutyCycle(50)

    # right motor
    PWMpinRF.ChangeDutyCycle(0) 
    PWMpinRB.ChangeDutyCycle(50)

    # let the platform move backward for the defined time
    sleep(delay)    
    # turn off the motors
    turn_off()
   

def turn_right(delay):
    # the function for turning RIGHT for the defined period of time
    # left motor
    PWMpinLF.ChangeDutyCycle(100) 
    PWMpinLB.ChangeDutyCycle(0)

    # right motor
    PWMpinRF.ChangeDutyCycle(0) 
    PWMpinRB.ChangeDutyCycle(100)

    # let the platform turn right for the defined time
    sleep(delay)    
    # turn off the motors
    turn_off()
    

def turn_left(delay):
    # the function for turning LEFT for the defined period of time
    # left motor
    PWMpinLF.ChangeDutyCycle(0) 
    PWMpinLB.ChangeDutyCycle(100)

    # right motor
    PWMpinRF.ChangeDutyCycle(100) 
    PWMpinRB.ChangeDutyCycle(0)

    # let the platform turn left for the defined time
    sleep(delay)    
    # turn off the motors
    turn_off()

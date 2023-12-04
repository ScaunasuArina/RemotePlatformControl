import RPi.GPIO as GPIO
import Adafruit_DHT

# set the pin numbering to GPIO.BCM in order to use the GPIO numering, not the physical one
GPIO.setmode(GPIO.BCM)

# set sensor type to DHT11
sensor = Adafruit_DHT.DHT11

# set GPIO pin on which sensor is connected to
dht11 = 4

# set the sensor as INPUT since this is used to receive data from the sensor
GPIO.setup(dht11, GPIO.IN)


def read_temperature_and_humidity():
    # the function which reads temperature and humidity
    humidity = 0
    temperature = 0
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht11)

    if humidity is not None and temperature is not None:
        print('Temperature = %.2f' % temperature, ' Humidity = %.2f' % humidity)

    else:
        print('Failed to get reading. Try again!')
        print(temperature, humidity)

    return temperature, humidity

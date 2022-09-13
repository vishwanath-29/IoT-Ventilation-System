
import sys

import Adafruit_DHT

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
# print(sys.argv[1])
# print(sensor_args[sys.argv[1]])
sensor = sensor_args['11']
pin = sys.argv[1]

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


# # temperature = temperature * 9/5.0 + 32

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

import RPi.GPIO as GPIO
from time import sleep
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1 = 11
pin2 = 15

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.IN)

while True: 
    if GPIO.input(pin2): 
        GPIO.output(pin1, GPIO.HIGH)
    else:
        GPIO.output(pin1, GPIO.LOW)


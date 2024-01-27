import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time
import sys
from time import sleep
from datetime import datetime
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

pin1 = 11
pin2 = 15
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(pin2, GPIO.IN)

debug = False
if '-debug' in sys.argv:
    debug = True

blinkrate = float(input('Enter the blink interval in seconds: '))
max_time = int(input('Enter the amount of time you want to run this in seconds: '))
iteration = 0

with open('data.txt', 'w') as data:
    start_time = time.time()
    while (time.time() - start_time) < max_time: 
        if GPIO.input(pin2):
            GPIO.output(pin1, GPIO.HIGH) # Turn on
            data.write(f'{time.time():1.0f}\t{GPIO.input(pin2)}\n')
            sleep(blinkrate / 2)                     
            GPIO.output(pin1, GPIO.LOW)  # Turn off
            data.write(f'{time.time():1.0f}\t{GPIO.input(pin2)}\n')
            sleep(blinkrate / 2)
            iteration += 1
        if debug: 
            date_t = datetime.fromtimestamp(time.time())
            print(f'Formatted Date : {date_t}\tNumber of Iteration : {iteration}\tSwitch State : {GPIO.input(pin2)}\n')
               
    

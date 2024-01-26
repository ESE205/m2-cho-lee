import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
import sys
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

if (len(sys.argv) > 1): n = int(sys.argv[1])
if (len(sys.argv) == 1): n = 5

pin1 = 11
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

while n > 0: # Run n times
   n -= 1 # Decrement counter
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   sleep(1)                     # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   sleep(1)                     # Sleep for 1 second
GPIO.cleanup()

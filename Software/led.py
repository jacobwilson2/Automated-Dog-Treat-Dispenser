import RPi.GPIO as GPIO
import time

RED = 21
GREEN = 16
YELLOW = 20

def initLED():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)

def ledControl(pin, state):
    GPIO.output(pin, state)

def redON():
    ledControl(RED, True)

def redOFF():
    ledControl(RED, False)

def yellowON():
    ledControl(YELLOW, True)

def yellowOFF():
    ledControl(YELLOW, False)

def greenON():
    ledControl(GREEN, True)

def greenOFF():
    ledControl(Green, False)

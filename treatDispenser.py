import RPi.GPIO as GPIO
import time

STEPPER_ON_OFF = 23
STEPPER_DIR_FWD = 18
STEPPER_CLOCK = 17
PUSH_BUTTON = 24

steps = 10500
def stepperInit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STEPPER_ON_OFF, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(STEPPER_DIR_FWD, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(STEPPER_CLOCK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def stepperSleep():
    GPIO.output(STEPPER_ON_OFF, False)


def gotoHome():
    forward(2000) # on this stepper, 1/64 of a turn is 1 step
    while GPIO.input(PUSH_BUTTON) != 0:
	backwards(10)
    backwards(250)
    stepperSleep()

def forward(steps):
  GPIO.output(STEPPER_ON_OFF, True) #turn stepper controller ON
  GPIO.output(STEPPER_DIR_FWD, True) #FWD
  for i in range(steps):
    GPIO.output(STEPPER_CLOCK, True) #Clock UP
    for j in range(1000): # time between Clock on and off
      pass

    GPIO.output(STEPPER_CLOCK, False) #Clock DOWN
    stepperSleep()

def backwards(steps):
  GPIO.output(STEPPER_ON_OFF, True) #turn stepper controller ON
  GPIO.output(STEPPER_DIR_FWD, False) #REVERSE
  for i in range(steps):
    GPIO.output(STEPPER_CLOCK, True) #Clock UP
    for j in range(1000):
      pass

    GPIO.output(STEPPER_CLOCK, False) #Clock DOWN
    stepperSleep()

def dispenseBiscuit():
    gotoHome()

    forward(steps)

    for i in range(1000000):
    	pass

    backwards(steps)

    for i in range(1000000):
    	pass

    forward(steps / 3)
    backwards(steps / 3)

    GPIO.output(STEPPER_ON_OFF, False)
    #print("Exit Normally")

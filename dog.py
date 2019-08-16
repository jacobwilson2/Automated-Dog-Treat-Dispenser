import led
import time
import rangefinder
import treatDispenser
import cameraControl
import sendPix

#initialize all modules
led.initLED()
treatDispenser.stepperInit()
treatDispenser.gotoHome()
led.greenON()

#global variables
elapsedTime = 0.0
startTime = 20
print(startTime)

while True:
    try:
        #if find_dog finds something in front of sensor, it returns True
        if rangefinder.find_dog():
            led.redON()
            print("FOUND DOG")
            if time.time() - startTime > 15:
                treatDispenser.dispenseBiscuit()
                startTime = time.time()
                cameraControl.takepicture()
                sendPix.sendPicture()
            else:
                print(time.time() - startTime)

        else:
            led.redOFF()
            print(time.time() - startTime)
            print("NO DOG")

        time.sleep(1)
    except KeyboardInterrupt:
        treatDispenser.stepperSleep()
        print("\nKeyboardInterrupt")
        print("\nStepper Enable Off")
        exit()

import picamera

camera = picamera.PiCamera()
print("initialized Camera")

def takepicture():
    camera.capture('image.jpg')

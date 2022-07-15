import RPi.GPIO as GPIO                 #Used to Import the LED
import time                             #Used to allow wait times
from picamera import PiCamera           #Used to import the Camera

from datetime import datetime

import os


camera = PiCamera()                     #Camera Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                  #Setting the GPIO Mode
GPIO.setup(22, GPIO.OUT)                #LED Flash Output
GPIO.setup(27, GPIO.OUT)                #LED indicator output

cwd = os.getcwd()                       #Sets the Current Working Directory




def bugmotion():
    GPIO.output(22, 0) #Sets light off

    print("\nProgram Running!")
    for i in range(3):
        time.sleep(1)
        GPIO.output(27, 1)
        time.sleep(1)
        GPIO.output(27, 0)
        if i == 3:
            break


    #To stabilize the Camera
    time.sleep(2)
    while True:

        #Turns on the LED Flash
        GPIO.output(22, 1)

        #Sets Img path and filename, Saves to Working directory of Script
        # Grab the current time
        filePath = cwd + "/Pictures/"
        currentTime = datetime.now()
        picTime = currentTime.strftime("%Y-%m-%d-%H-%M-%S")
        picName = "Capture-" + picTime + '.jpg'
        completeFilePath = filePath + picName
        #file_name = cwd + "/Pictures/Capture_" + str(time.time()) + ".jpg"
        print("\nFile Name is: " + completeFilePath)


        #Used to wait for 0.1 Seconds for Camera to be ready
        time.sleep(0.1)

        #Saves File
        camera.capture(completeFilePath)

        #Used to turn off the LED after 0.2 Secs
        time.sleep(0.2)

        #Used to turn off the LED
        GPIO.output(22, 0)

        #Used to wait 5 minutes for camera to take a photo
        time.sleep(300)
        print("\nTaking photo!")

def exit_handler():
    print('Program Shutting Down!')
    GPIO.output(22, 0) # turns off LED

bugmotion() #Starts Program
atexit.register(exit_handler)







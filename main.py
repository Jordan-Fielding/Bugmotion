import RPi.GPIO as GPIO                 #Used to Import the LED
import time                             #Used to allow wait times
from picamera import PiCamera           #Used to import the Camera
from gpiozero import MotionSensor       #Used to import the MotionSensor
from datetime import datetime
from subprocess import call
import os

pir = MotionSensor(4)
camera = PiCamera()                     #Camera Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                  #Setting the GPIO Mode
GPIO.setup(22, GPIO.OUT)                #LED output pin

cwd = os.getcwd()                       #Sets the Current Working Directory




def bugmotion():
    GPIO.output(22, 0) #Sets light off

    print("\nProgram Running!")

    #To stabilize sensor and Camera
    time.sleep(2)
    while True:

        #Waits for Motion from PIR Sensor
        pir.wait_for_motion()

        print("\nBug detected")

        #Turns on the LED Flash
        GPIO.output(22, 1)

        #Sets Img path and filename, Saves to Working directory of Script
        # Grab the current time
        filePath = cwd + "/Pictures/"
        currentTime = datetime.now()
        picTime = currentTime.strftime("%Y.%m.%d-%H%M")
        picName = "Capture-" + picTime + '.jpg'
        completeFilePath = filePath + picName
        #file_name = cwd + "/Pictures/Capture_" + str(time.time()) + ".jpg"
        print("\nFile Name is: " + completeFilePath)


        #Used to wait for 0.1 Seconds for Camera to be ready
        time.sleep(0.1)

        #Saves File
        camera.capture(completeFilePath)

        #Sets PIR Sensor back to waiting for motion
        print("\nWaiting for no Motion!")
        pir.wait_for_no_motion()

        #Used to turn off the LED after 0.2 Secs
        time.sleep(0.2)

        #Used to turn off the LED
        GPIO.output(22, 0)

        #Used to stabilize Sensor and allow the Camera to refocus
        time.sleep(2)
        print("\nSystem Ready!")

def exit_handler():
    print('Program Shutting Down!')
    GPIO.output(22, 0) # turns off LED

bugmotion() #Starts Program
atexit.register(exit_handler)







import RPi.GPIO as GPIO                 #Used to Import the LED
import time                             #Used to allow wait times
from picamera import PiCamera           #Used to import the Camera
from gpiozero import MotionSensor       #Used to import the MotionSensor
import os

pir = MotionSensor(4)
camera = PiCamera()                     #Camera Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                  #Setting the GPIO Mode
GPIO.setup(22, GPIO.OUT)                #LED output pin

cwd = os.getcwd()                       #Sets the Current Working Directory


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
    file_name = cwd + "/Pictures/Capture_" + str(time.time()) + ".jpg"
    print("\nFile Name is: " + file_name)


    #Used to wait for 0.1 Seconds for Camera to be ready
    time.sleep(0.1)

    #Saves File
    camera.capture(file_name)

    #Sets PIR Sensor back to waiting for motion
    pir.wait_for_no_motion()

    #Used to turn off the LED after 0.2 Secs
    time.sleep(0.2)

    #Used to turn off the LED
    GPIO.output(22, 0)

    #Used to stabilize Sensor and allow the Camera to refocus
    time.sleep(2)
    print("\nSystem Ready!")









import RPi.GPIO as GPIO                 #Used to Import the LED
import time                             #Used to allow wait times
from picamera import PiCamera           #Used to import the Camera
from gpiozero import MotionSensor       #Used to import the MotionSensor
import os

pir = MotionSensor(4)
camera = PiCamera()                     #Camera Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                  #Setting the GPIO Mode
GPIO.setup(22, GPIO.OUT)

cwd = os.getcwd()

#LED output pin


#To stabilize sensor and Camera
time.sleep(2)
while True:

    #Waits for Motion from PIR Sensor
    pir.wait_for_motion()

    print("Bug detected")

    #Turns on the LED Flash
    GPIO.output(22, 1)

    #Sets Img path and filename, Saves to USB Connected
    print("File will be Saved in: " + cwd)
    file_name = cwd +"/Capture_" + str(time.time()) + ".jpg"


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

    print("Bug Not Detected")









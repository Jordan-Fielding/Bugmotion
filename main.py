import RPi.GPIO as GPIO #Used to Import the LED
import time #Used to allow wait times
from picamera import PiCamera #Used to import the Camera
from gpiozero import MotionSensor #Used to import the MotionSensor

pir = MotionSensor(4)
camera = PiCamera() #Camera Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #Setting the GPIO Mode
GPIO.setup(22, GPIO.OUT) #LED output pin



time.sleep(2) # to stabilize sensor and Camera
while True:

    pir.wait_for_motion()
    print("Bug detected")
    GPIO.output(22, 1)
    file_name = "/home/qldcomp/Pictures/img_" + str(time.time()) + ".jpg"
    camera.capture_sequence(file_name)
    pir.wait_for_no_motion()
    time.sleep(1)
    GPIO.output(22, 0)
    print("Bug Not Detected")









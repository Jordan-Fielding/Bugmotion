import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.OUT)         #LED output pin

i=GPIO.input(11)

time.sleep(2) # to stabilize sensor
while True:
    #ts = time.time()
    #st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    if i==0:                 #When output from motion sensor is LOW
        print ("No bugs detected",i)
        GPIO.output(13, 0)  #Turn OFF LED
        time.sleep(2)
    if i==1:               #When output from motion sensor is HIGH
        print("bugs detected",i)
        GPIO.output(13, 1)  #Turn ON LED
        camera.capture('/home/pi/Pictures/img.jpg')
        print("Photo Saved")
        #os.system('libcamera-jpeg -o /home/pi/Pictures/image_Time_{}.jpg'.format(st))
        camera.close()  #Capture an Image
        time.sleep(2)







import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(27, GPIO.OUT)         #LED output pin

i=GPIO.input(22)

time.sleep(2) # to stabilize sensor
while True:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    if i==0:                 #When output from motion sensor is LOW
        print ("No bugs detected",i)
        GPIO.output(3, 0)  #Turn OFF LED
        time.sleep(0.1)
    if i==1:               #When output from motion sensor is HIGH
        print ("bugs detected",i)
        GPIO.output(3, 1)  #Turn ON LED
        camera.capture('image_Time_{}.jpg'.format(st))
        os.system('libcamera-jpeg -o /home/pi/Pictures/image_Time_{}.jpg'.format(st))
        camera.close()  #Capture an Image
        time.sleep(0.1)







leg1.pyth
#import lib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#set GPIO number Mode
GPIO.setup(11,GPIO.OUT)
servo1=GPIO(11,50)

print("servo1 is ready to move")

#PULSE OFF,PWM RUNNING
servo1.start(0)
time.sleep(2)

#define variables duty
duty = 0

print(" move 180 deg in 10 steps")

#loop duty 2 to 12(0 to 180 deg)
while duty<=10:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty=duty+1
    
#back to 90
print("back normal position")
servo1.ChangeDutyCycle(7)
time.sleep(2)

#to 0 deg
servo1.ChangeDutyCycle(2)
time.sleep(0.5)


#stop
servo1.stop()
GPIO.cleanup()
print("done")

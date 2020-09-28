import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14,RPi.GPIO.OUT)

pwm = RPi.GPIO.PWM(14,80)

pwm.start(0)

try:
    while True:
        for i in range(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
        
        for i in range( 100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
            
except KeyboardInterrupt:
    pass

pwm.stop()

RPi.GPIO.cleanup()
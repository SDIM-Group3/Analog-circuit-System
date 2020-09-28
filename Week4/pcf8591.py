import smbus
import time
import RPi.GPIO as GPIO
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
	global address
	address = Addr
def read(chn): #channel
	try:
		if chn == 0:
			bus.write_byte(address,0x40)
		if chn == 1:
			bus.write_byte(address,0x41)
		if chn == 2:
			bus.write_byte(address,0x42)
		if chn == 3:
			bus.write_byte(address,0x43)
		bus.read_byte(address) # dummy read to start conversion
	except Exception, e:
		print "Address: %s" % address
		print e
	return bus.read_byte(address)
def write(val):
	try:
		temp = val # move string value to temp
		temp = int(temp) # change string to integer
# print temp to see on terminal else comment out
		bus.write_byte_data(address, 0x40, temp)
	except Exception, e:
		print "Error: Device address: 0x%2X" % address
		print e

if __name__ == "__main__":
		setup(0x48)
led_pin = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(37, 80)
pwm.start(0)
try:
	while True:
		print 'AIN0 = ', read(0)
		print 'AIN1 = ', read(1)
		print 'AIN2 = ', read(2)
		print 'AIN3 = ', read(3)
		print ' '
		tmp = read(0)
		tmp = tmp*(255-125)/255+125 # LED won't light up below 125, so convert '0-255' to '125-255'
		write(tmp)
		print("tmp=")
		print(tmp)
		tryy = (tmp-125)
		if tryy < 0:
			tryy = 0;
		if tryy > 100:
			tryy = 100
		pwm.ChangeDutyCycle(tryy)
		#GPIO.output(37,GPIO.HIGH)
		time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()

# Following code is tested with Raspberry Pi 3
# Import the Libraries Required
import RPi.GPIO as GPIO
import time
import random
import socket
from struct import *

SERVO_PIN = 32

def ang2duty (angle):
	DutyCycle = (angle/18) + 2
	return DutyCycle

if __name__ == '__main__':
	# Setting the GPIO Mode to BOARD => Pin Count Mapping 
	GPIO.setmode(GPIO.BOARD)

	# Setting the GPIO Mode to BCM => GPIO Mapping 
	# Uncomment below line for to use GPIO number
	# GPIO.setmode(GPIO.BCM)

	# Setting the GPIO 18 as PWM Output 
	GPIO.setup(SERVO_PIN,GPIO.OUT)

	# Disable the warning from the GPIO Library
	GPIO.setwarnings(False)

	# Starting the PWM and setting the initial position of the servo with 50Hz frequency 
	servo = GPIO.PWM(SERVO_PIN,50)
	servo.start(0)

	#UDP_IP = "96.49.100.238"
	#UDP_IP = "127.0.0.1"
	# UDP_IP = socket.gethostbyname(socket.gethostname())
	UDP_IP = "172.20.10.11"
	print ("Receiver IP: ", UDP_IP)
	#UDP_PORT = 6000
	# UDP_PORT = int(raw_input ("Enter Port "))
	UDP_PORT = 5555
	print ("Port: ", UDP_PORT)   
	sock = socket.socket(socket.AF_INET, # Internet
						socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))

	while True:
		try:
			# randang = random.randint(0, 180)
			# d = ang2duty(randang)
			# Changing the Duty Cycle to rotate the motor 
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
			x = "%1.f" %unpack_from ('!f', data, 36)
			print(x)
			conv = int(x) + 90
                        if conv < 0 :
                                conv = 0
                        elif conv > 180:
                                conv = 180
			d = ang2duty(conv)
			servo.ChangeDutyCycle(d)
			print("Current angle is {} degrees".format(conv))
			# Sleep for 5 Seconds 
			time.sleep(0.2)

		except KeyboardInterrupt:
			servo.stop()
			GPIO.cleanup()
# End of the Script

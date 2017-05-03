import serial
import time
from datetime import datetime
i = datetime.now()
def send_text(number, text, path='/dev/modem0'):
	ser = serial.Serial(path, timeout=1)
	ser.write('AT+CMGF=%d\r' % 1)
	time.sleep(2)
	print ser.readlines()
	ser.write('AT+CMGS="%s"\r' % number)
	time.sleep(2)
	print ser.readlines()
	ser.write('%s\x1a' % i)
	time.sleep(2)
	print ser.readlines()
	ser.close()

time.sleep(30)
send_text('085294563126', 'test from 2g-iot?')

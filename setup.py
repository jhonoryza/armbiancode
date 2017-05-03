import serial
import time
ser = serial.Serial('/dev/modem0', timeout=1)
ser.write('AT+COPS=%d\r' % 0)
time.sleep(5)
print ser.readlines()
ser.close()

import serial
import time

ser = serial.Serial('COM5', 250000)
time.sleep(1)
# ser.write(b'G0 Y10\n')
# time.sleep(0.2)

ser.write(bytes('G91' + '\n', 'UTF-8'))

ser.write(bytes('M302 P1' + '\n', 'UTF-8'))

# ser.write(bytes('M203 E5' + '\n', 'UTF-8'))
# time.sleep(0.2)

ser.write(bytes('T0' + '\n', 'UTF-8'))

ser.write(bytes('G0 Y10' + '\n', 'UTF-8'))

ser.write(bytes('G0 E1.6' + '\n', 'UTF-8'))

ser.close()
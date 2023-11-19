import serial
import time

dev = serial.Serial("COM5", 19200)


sol_f = open("solution.txt","r")
sol_l = sol_f.readlines()

for i in sol_l:
    i = i[0,1]
    
    dev.write(i.encode())
    time.sleep(0.1)


sol_f.close()
dev.close()
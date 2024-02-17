from datetime import date
import serial
import os

# os.execv("rm -f ./data/*")

# Test directories creation
today = str(date.today())
try:
    os.mkdir(today)
except OSError as error:
   print(error)

electrode = today + "/t5-c3"
try:
    os.mkdir(electrode)
except OSError as error:
   print(error)

data = electrode
try:
    os.mkdir(data)
except OSError as error:
    print(error)

serial_inst = serial.Serial()
serial_inst.port = '/dev/ttyACM0'
serial_inst.baudrate = 115200
serial_inst.open()

file_name = data + '/NO.csv'
while True:
    if serial_inst.in_waiting:
        value = serial_inst.read()
        print(value.decode('utf'))
        file = open(file_name,'ab')
        file.write(value)
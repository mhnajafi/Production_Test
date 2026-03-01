import serial
from time import sleep
from tests import *
import esptool
import pystlink 
#ser = serial.Serial ("/dev/ttyS0", 115200)    #Open port with baud rate
#while True:
#    received_data = ser.read()              #read serial port
#    sleep(0.03)
#    data_left = ser.inWaiting()             #check for remaining byte
#    received_data += ser.read(data_left)
#    print (received_data)                   #print received data
    # ~ ser.write(received_data)                #transmit data serially 
#print(Command_json("microphone","test",555))

#send_json("zone","all",5000)
#print(Command_json_esp("setDevice","file set",0,False))

# command = ['--help']
result_esp=""
try:
    stlnk = pystlink.PyStlink()
    ret=stlnk.start()
    print(ret)
    result_esp="OK"
except Exception as e:
    result_esp="ESP flash Err"
    print(e)

__author__ = 'Chetan'

import serial
import re
import time
import datetime
from collections import deque

ser = serial.Serial(
    port = 'COM8',\
    baudrate=9600,\

)

f = open("pressure.csv", "w")
#f.write("Test 1" +  "\n")
#f.write("Time - " + str(time.ctime()));
f.write(str(datetime.datetime.now())+ "\n")
startime =  time.clock()
f.write(str(startime)+ "\n")
f.write("StartTime" +  "," + "Signal recieved Time" +"," + "elasped time" + "," + "Analog" + "," + "Pressure(Kpa)" + "\n")
print("connected to: " + ser.portstr)
p = re.compile('\r')
n = re.compile('\n')
buffer = deque([])

ellasped = 0

def readDataFromSerial():
    while KeyboardInterrupt:
        value = ""
        for line in ser.readline():
            #print line
            #data is coming in x0dx0dxoa format
            #I am removing x0d which is \r in the input string and not needed
            # After removing only x0A i.e. \n remains which is good for populating
            #pressure sensor data into datastructure or file for post processing.
            if(not (p.match(line))):
                # sensor sends one bit at a time. Following code will combine bits
                # based on the data terminator as said above.
                # updating temp when \r is matched and writing the value of temp to buffer and file
                # when \n is matched
                if(not (n.match(line))):
                    value = value + line
                    #print line
                elif(n.match(line)):
                    ellasped = (time.clock() - startime)
                    #print str(time.clock()) + "," + str(startime) + "," + str(ellasped) >> f
                    analog = int(value)
                    buffer.append(value)
                    # translation function derived from comparing analog values from sensor and
                    # digital pressure gauge. This gives air pressure changes during walking or using UPS.
                    pressure = (0.3436 * analog - 156.82)
                    # log data with timestamp for post experiment analysis.
                    # Date : 2017/04/19
                    # now we find stiffness(spring constant) and dissipation factor
                    # stiffness is;
                    # f(x,y) = p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2 + p30*x^3 + p21*x^2*y + p12*x*y^2
                    # + p03*y^3 + p40*x^4 + p31*x^3*y + p22*x^2*y^2 + p13*x*y^3 + p04*y^4
                    # where
                    # x = applied load get this from load cell sensor i.e. Bridge-simple_loadcell.py
                    # y = input pressure

                    '''
                    stiffness = 2.362 + 192.6 * x - 843 * pressure -136.9 * pow(x,2) + 1436 * x * pressure \
                                + 11350 * pow(pressure, 2) + 45.34 * pow(x, 3)\
                                - 604 * pow(x, 2) * pressure - 998.3 * x * pow(pressure,2) - 46810.00 * pow(pressure, 3)\
                                -4.566 * pow(x,4) + 69.1 * pow(x,3) * pressure\
                                -155.9 * pow(x,2) * pow(pressure,2) + 6112 * x * pow(pressure, 3) + 61390 * pow(pressure, 4)

                    dissipation = 0.08225 + 0.4154 * x - 2.29 * pressure + 0.1038 * pow(x,2) - 0.4672 * x * pressure\
                                  +7.912 * pow(pressure, 2) - 0.01156 * pow(x,3) + 0.274 * pow(x,2) * pressure\
                                  - 5.688 * x * pow(pressure,2)
                    '''

                    f.write(str(startime) + "," + str(time.clock()) + "," + str(ellasped) + "," + value + "," + str(pressure)+ "\n")
                    value = ""

    ser.close()
    f.close()




def readBuffer():
    while (len(buffer) == 0):
        f.write(buffer.appendleft())

def main():
    readDataFromSerial()
    #readBuffer()
    print buffer
    print len(buffer)

main()
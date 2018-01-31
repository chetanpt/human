__author__ = 'Chetan'
'''
Requirement of this program:

Need Time in terms of seconds and milliseconds for loadcell and pressure sensor data visualization.
(Because previous use of datetime.now() gave seconds and microseconds but in excel it got messed up. Due to
same time the data shows stacked up at single point on X-axis.
I used GS_timing module from https://github.com/ElectricRCAircraftGuy/PyTiming to print time in terms of
microsecond of milliseconds.

For Loadcell:
Phidget bridge can update data for every 8 ms therefore 1000/8 = 125 samples per seconds. I need to print time
for every 8 ms so that time from 0 to n can be seen on X-axis
 - delayMicroseconds(8000)
 - number of records = 108
print/save time from 0 to N

For Pressure Sensor:
Pressure sensor with arduino provided ~191 samples per seconds i.e. One sample per 5.2 milliseconds. Therefore
I need to print the time in milliseconds for every 5 milliseconds
 - delayMicroseconds(5000)
 - number of records = 246
print/save time from 0 to N

Save the file in the Onedrive in

'''
from GS_timing import *

f = open("timeInms_for_loadcell.csv", "w")
t_start = micros()
delayMicroseconds(304000)
for x in range(0,108):
 delayMicroseconds(8000)
 t_end = micros() #us
 elaspedtime = t_end - t_start
 f.write(str(t_start) + "," + str(t_end)+ "," + str(elaspedtime)+ "\n")

'''
#print millis()
#print micros()
t_start = micros() #us
delayMicroseconds(8000)
t_end = micros() #us
elaspedtime = t_end - t_start
print(t_end)
print(t_start)
print(str(elaspedtime))
'''








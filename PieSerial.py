import serial
import numpy as np
from time import sleep
import json

import pandas as pd
import simplejson as js



ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port

counter = 32

AccList = []
f = 0

R = '{"sensor":"gps","time":1351824120,"data":[48.756080,2.302038]}'

while f < 100:
    # counter += 1
    # ser.write(str(chr(counter)))
    Q = ser.readline()  # Read the newest output from the Arduino
    Z = [x.strip() for x in Q.split(',')]
    AccList.append(Z)
    f+=1
    print Z
    #S = float(Z[0])
      # print three
    # print three['X']

    #break


    #print r
    # j = json.loads(Q)
    # print str(j)
    #sleep(.1)  # Delay for one tenth of a second

print AccList


#D = [[''], ['1.00', '0.01', '0.11'], ['1.00', '0.01', '0.11'], ['0.99', '0.02', '0.11'], ['1.02', '0.01', '0.09'], ['0.23', '0.2', '0.']]
C = np.column_stack(AccList[1:])

dk = pd.DataFrame({"X": C[0], "Y": C[1], "Z": C[2]})
print dk


writer = pd.ExcelWriter('/home/pavan/PAVANKUMAR/MachineLearning/MyFolder/DataFiles/Accelerometer_Xaxis.xlsx', engine='xlsxwriter' )
dk.to_excel(writer, 'accFile')
writer.save()


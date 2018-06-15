import pandas as pd
import math
import numpy


file = ".xlsx"

Time = pd.read_excel(file, sheetname="Time", skiprows=0)
Pressure = pd.read_excel(file, sheetname="Pressure", skiprows=0)
Rate = pd.read_excel(file, sheetname="Rate", skiprows=0)
TimeRate = pd.read_excel(file, sheetname="TimeRate", skiprows=0)
RealRate = pd.read_excel(file, sheetname="RealRate", skiprows=0)
TimeN = pd.read_excel(file, sheetname="TimeN", skiprows=0)

Time = numpy.array(Time)
Pressure = numpy.array(Pressure)
Rate = numpy.array(Rate)
TimeRate = numpy.array(TimeRate)
RealRate = numpy.array(RealRate)
TimeN = numpy.array(TimeN)
Time = Time[1:]
Pressure = Pressure[1:]
Rate = Rate[1:]
TimeRate = TimeRate[1:]


j=0
k=Pressure[0]
rRate = 0

# Use rate to find the referencepoint for pressure, then use that reference in every transient instead of starting from 0
#(F114-F113)/$F$83
#	Val = E86/$F$85

#Normalizes rate
for i in range(len(Time)):
    if j <= len(Rate):
        if RealRate[i] != RealRate[i-1]:
            j = j + 1
            if RealRate[i] > RealRate[i-1]:
                #print("Rate:", RealRate[i-1], " : ", RealRate[i])
                if(((Rate[j-1]-Rate[j-2])/6742) < 0 ):
                    val = (Rate[j - 1] - Rate[j - 2]) / 6724
                    print(TimeN[i] / val * -1)
                    #print(val)
                else:
                    print(0)
                rRate = 0
                #print( rRate)
            elif RealRate[i] < RealRate[i-1]:
                if (((Rate[j - 1] - Rate[j - 2]) / 6742) < 0):
                    val = (Rate[j - 1] - Rate[j - 2]) / 6724
                    print(TimeN[i] / val * -1)
                    #print(val)

                else:
                    print(0)
                    #print(val)

                rRate = 0
               # print("Rate1:", RealRate[i-1], " : ", RealRate[i])
              #  print("B", (Rate[j-1]-Rate[j-2])/6742)

                rRate = RealRate[i] - RealRate[i-1]
               # print( rRate)

        #elif RealRate[i] == RealRate[i-1]:
        else:
            if (((Rate[j - 1] - Rate[j - 2]) / 6742) < 0):
                val = (Rate[j - 1] - Rate[j - 2])/6724
                print(TimeN[i]/val *-1)
                #print(val)

            else:
                #   print(val)

                print(0)
            rRate = 0
            #print((Rate[j-1]-Rate[j-2])/6742)
            #print("Rate2:", RealRate[i - 1], " : ", RealRate[i])

            #print(rRate)
'''

      #This finds the pressure for [i] compared to the previous period
      
        #print("TM:  ", Time[i])
for i in range(len(Time)):
    if j <= len(Rate):
        if RealRate[i] != RealRate[i-1]:
            if RealRate[i] < RealRate[i-1]:
                if (Pressure[i] - k) > 0:

                    print(Pressure[i] - k)
                else:
                    print(0)
                #print("PB: ", Pressure[i] - k, "T: ", Time[i])
                k = Pressure[i]

            elif RealRate[i] > RealRate[i - 1]:
                if (Pressure[i] - k) > 0:
                    print(Pressure[i] - k)
                else:
                    print(0)
               # print("PS: ", Pressure[i] - k, "T: ", Time[i])
                k = Pressure[i]

                # print("P: ",  Pressure[i], " K: ", k)

         #   k = Pressure[i]
            #print("b")
            j +=1


        elif RealRate[i] == RealRate[i-1]:
            if (Pressure[i] - k) > 0:
                print(Pressure[i] - k )
            else:
                print(0)
                

        
     ## Prints the pressure 
         if j <= len(TimeRate):
        if RealRate[i] != RealRate[i-1]:
            if RealRate[i] > RealRate[i-1]:
                print("Rate:", Rate[j-1], " : ", Rate[j])
                rRate = 0
                j = j+1
                #print( rRate)
            elif RealRate[i] < RealRate[i-1] and RealRate[i] < -50:
                print("Rate1:", Rate[j-1], " : ", Rate[j])

                rRate = RealRate[i] - RealRate[i-1]
               # print( rRate)

        elif RealRate[i] == RealRate[i-1]:
            print("Rate2:", Rate[j - 1], " : ", Rate[j])

            #print(rRate)
      '''
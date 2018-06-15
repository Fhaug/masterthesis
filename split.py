import math
import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
Time =[
]

Pressure=[
]

Time2=[
]
Pressure2=[
]

Time3 = [
]
Pressure3=[
]

Time4 = [
]
Pressure4 = [
]

Time5 = [
]

Pressure5 = [
]

Time6 = [
]
Pressure6 = [
]


TimeB=[
]

PressureB = [
]

TimeB2 = [
]

PressureB2 = [
]

TimeB3 = [
]

PressureB3 = [
]

TimeB4 = [
]

PressureB4 = [
]

TimeB5 = [
]

PressureB5 = [
]

TimeB6 = [
]

PressureB6 =[
]


TimeSplit = [0.5,1, 5, 10, 50, 100,150, 190, 200, 300]
def func(x,a,b,c):
   return a*x**b+c

print("TIMESPLIT: ", TimeSplit)
j = 0
k = 0
def split(var1, var2):
    j = 0
    k = 0
    testTime = []
    testPressure = []
    param_bounds = ([-np.inf, 0, -np.inf], [np.inf, 2, np.inf])

    for i in range(len(var1)):
        if var1[i] > TimeSplit[j]:
            try:
                print(var1[k], var1[i])
                #print(testTime)
                popt, pcov = curve_fit(func, TimeB, PressureB, bounds=param_bounds)
                plt.plot(TimeB, func(TimeB, *popt), 'b-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
                print('%5.3f*x**%5.3f + %5.3f' %tuple(popt))
                print(popt[0]*2**popt[1] + popt[2])
                print(var2[i], var2[k], var1[i], var1[k])
                print("Degrees: Timesplit:",TimeSplit[j], math.degrees(math.atan2(var2[i]-var2[k], var1[i]-var1[k])))
                print("Length: Timesplit:",TimeSplit[j], math.hypot(var2[i]-var2[k], var1[i]-var1[k]))
                print("Slope: Timesplit:",TimeSplit[j] , (var2[i]- var2[k])/(var1[i] - var1[k]))
                j+=1
                k=i
            except:
                print("1")
        elif i+1 == len(var1):
            print("Degrees: Timesplit:",TimeSplit[j], math.degrees(math.atan2(var2[i]-var2[k], var1[i]-var1[k])))
            print("Lengh: Timesplit:",TimeSplit[j], math.hypot(var2[i]-var2[k], var1[i]-var1[k]))
            print("Slope: Timesplit:",TimeSplit[j] , (var2[i]- var2[k])/(var1[i] - var1[k]))

        #print()
        #print(Time[k], Time[i])

split(TimeB, PressureB)
print("-------------")
split(TimeB2, PressureB2)
print("-------------")
split(TimeB3, PressureB3)
print("-------------")
split(TimeB4, PressureB4)
print("-------------")
split(TimeB5, PressureB5)
print("-------------")
split(TimeB6, PressureB6)

#print(func(Time, *popt))
print()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.show()
'''elif i+1 == len(var1):
    popt, pcov = curve_fit(func, var1, var2, bounds=param_bounds)
    plt.plot(var1, func(var1, *popt), 'b-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    print("Slope: ", (var2[i]- var2[k])/(var1[i] - var1[k]))
    testTime.clear()
    testPressure.clear()
    else:
    print(var1[i], var2[i])
    testTime.append(var1[i])
    testPressure.append(var2[i])
        '''
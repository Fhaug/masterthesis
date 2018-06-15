import pandas as pd
import math

#Input
command = input("Find amplitudes or double file (amp/fil): ")
type(command)
file = "time.xlsx"
timeData = pd.read_excel(file,  sheetname="Sheet2")
timeRateData = pd.read_excel(file,  sheetname="Sheet1")
rateData = pd.read_excel(file,  sheetname="Sheet3")

#Converting the dataFrame into tuples, to use it effectivly in python
timeList = [list(x) for x in timeData.values]
timeRateList = [list(x) for x in timeRateData.values]
rateList = [list(x) for x in rateData.values]
#pressureTuple.pop(0)
secondPressure =[]
n = 0
k = 0
print("ratelist[0]: " , rateList[0])
print("timeratelist[0]: " , timeRateList[0])
print("time[0]: " , timeList[0])
3135,432804

if command == "fil":
    for i in range(len(timeList)):
        if timeList[i] == timeRateList[n]:
            secondPressure.append(rateList[k])
            n +=1
            k +=1
        else:
            secondPressure.append(rateList[k])

    writer = pd.ExcelWriter("data1.xlsx", engine="xlsxwriter")
    df = pd.DataFrame({"pressure" : secondPressure})
    df.to_excel(writer, sheet_name="Sheet1")
    writer.save()
    print("PRESSURE: ", len(secondPressure))
    print("TIME: ", len(timeList))

elif command == "amp":
    for i in range(len(pressureTuple)):
        if len(pressureTuple)-i >=3:
            if pressureTuple[i] > pressureTuple[i-2] and pressureTuple[i] > pressureTuple[i+2]:
                print("amplitude_high: ", i, "Rewrite high to 5000, low to  2000", "::::: High is :", pressureTuple[i])
                secondPressure[i] = "5000"
                secondPressure[i-1] = "2000"

            elif pressureTuple[i] < pressureTuple[i+2] and pressureTuple[i] < pressureTuple[i-2]:
                print("amplitude_low: ", i, "Rewrite high to 5000, low to  2000", ":::::: Low is :", pressureTuple[i])
                secondPressure[i] = "5000"
                secondPressure[i-1] = "2000"

            elif pressureTuple[i] > pressureTuple[i-2]:
                secondPressure[i] = ""

            else:
                secondPressure[i] = ""
        else:

            if pressureTuple[i]>pressureTuple[i-2]:
                print("amplitude_high: ", i, "Rewrite high to 5000, low to  2000", "::::: High is :", pressureTuple[i])
                secondPressure[i] = "5000"
                secondPressure[i-1] = "2000"

            else:
                print("amplitude_low: ", i, "Rewrite high to 5000, low to  2000", "::::: Low is :", pressureTuple[i])
                secondPressure[i] = "5000"
                secondPressure[i-1] = "2000"

    for i in range(len(secondPressure)):
        if secondPressure[i] == "2000" and secondPressure[i+1] == "2000":
            secondPressure[i] = ""

  #  writer = pd.ExcelWriter("time.xlsx", engine ="xlsxwriter")
   # df = pd.DataFrame({"Pressure" : secondPressure})
    #df.to_excel(writer, sheet_name="Sheet2")
    #writer.save()

    print(secondPressure)
    print("Pandas imported")
else:
    print("invalid command, closing prog")
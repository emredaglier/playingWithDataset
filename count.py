# A Python program to count class numbers according to the YOLO label files
# Author: Emre Daglier
# emredaglier@gmail.com

import os

classes = {}

def printTable(myDict, colList=None): #Author: Thierry Husson
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))

for file in os.listdir('.'):                            #
    if file.endswith('.txt') and file != 'classes.txt': #
        try:                                            #
            with open(file) as filePath:                #
                line = filePath.readline()              #
                while line:                             #
                    if line.split()[0] not in classes:  #   In this block, we initialize the class numbers in the key part of our dictionary
                        classes[line.split()[0]] = 0    #
                    line = filePath.readline()          #
        finally:                                        #
            filePath.close()                            #


for file in os.listdir('.'):                            #
    if file.endswith('.txt') and file != 'classes.txt': #
                                                        #
        try:                                            #
            with open(file) as filePathCount:           #
                line = filePathCount.readline()         #   In this block, we calculate the number of classes according to the text files and initialize the final calculation to our dictionary
                while line:                             #
                    classes[line.split()[0]] += 1       #
                    line = filePathCount.readline()     #
        finally:                                        #
            filePathCount.close()                       #

printTable([classes])
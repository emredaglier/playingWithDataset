import os

classes = {}

arr = os.listdir('.')

def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))

for file in os.listdir('.'):
    if file.endswith('.txt') and file != 'classes.txt':
        try:                                            #
            with open(file) as filePath:                #
                line = filePath.readline()              #
                while line:                             #
                    if line.split()[0] not in classes:  # In this block, we initialize the class numbers
                        classes[line.split()[0]] = 0    #
                    line = filePath.readline()          #
        finally:                                        #
            filePath.close()                            #


for file in os.listdir('.'):
    if file.endswith('.txt') and file != 'classes.txt':

        try:
            with open(file) as filePathCount:
                line = filePathCount.readline()
                while line:
                    classes[line.split()[0]] += 1
                    line = filePathCount.readline()

                


        finally:
            filePathCount.close()

sorted(classes)
printTable([classes])
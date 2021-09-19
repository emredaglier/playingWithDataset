import os

classes = {}

arr = os.listdir('.')

for file in os.listdir('.'):
    if file.endswith('.txt'):
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
    if file.endswith('.txt'):

        try:
            with open(file) as filePathCount:
                line = filePathCount.readline()
                while line:
                    classes[line.split()[0]] += 1
                    line = filePathCount.readline()

                


        finally:
            filePathCount.close()




print(classes)
        



#count = len(open(file).readlines(  ))
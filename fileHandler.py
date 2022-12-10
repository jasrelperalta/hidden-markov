def openFile(filePath):
    f = open(filePath, 'r')

    numString = int(f.readline().strip())

    stringList = []
    for i in range(numString):
        # dynamic strings
        stringList.append(f.readline().strip())

    stateList = f.readline().strip().split(' ')
    measureList = f.readline().strip().split(' ')
    
    valList = []
    valList.append(f.readline().strip().split(' '))
    valList.append(f.readline().strip().split(' '))

    resList = []
    for i in range(int(f.readline().strip())):
        # dynamic cases
        resList.append(f.readline().strip().split(' given '))

    return numString, stringList, stateList, measureList, valList, resList
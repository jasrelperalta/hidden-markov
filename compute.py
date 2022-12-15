def getMaxStateNeeded(resList):
    max = 0
    for res in resList:
        for pair in res:
            if max < int(min(pair)):
                max = int(min(pair))
    return max


def getOtherState(state, stateList):
    other = ''
    if state == stateList[0]:
        other = stateList[1]
    else:
        other = stateList[0]
    return other


def countOccurence(state, stringSeq):
    count = 0
    for letter in stringSeq[:len(stringSeq)-1]:
        if state == letter:
            count += 1
    return count


def countFollowedBy(state1, state2, stringSeq):
    count = 0
    for i in range(len(stringSeq)-1):   # -1 so it wont go out of range
        if stringSeq[i] == state1 and stringSeq[i+1] == state2:
            count += 1
    return count


def getInitStates(stateList, stringSeq):
    otherState = getOtherState(stringSeq[0], stateList)
    return {stringSeq[0]:[1], otherState:[0]}


def printStates(dataProb):
    for i in dataProb:
        print(i, dataProb[i])


def totalProbability(state, otherState, n, dataProb):
    result = 0

    tempStr = str(state) + '|' + str(state)

    result = dataProb[tempStr]* dataProb[state][n-1]

    tempStr = str(state) + '|' + str(otherState)

    result += dataProb[tempStr] * dataProb[otherState][n-1]

    return result


def getMeasureDict(stateList, measureList, valList):
    tempDict = {}
    for i in range(0, len(measureList)):  # two values only
        for j in range(0, len(stateList)):
            tempStr = measureList[i] + '|' + stateList[j]
            tempDict[tempStr] = float(valList[j][i])

    return tempDict


def getMeasureProbability(measure, stateList, n, dataProb):
    res = 0
    
    for state in stateList:
        tempStr = str(measure) + '|' + str(state)
        
        res += dataProb[tempStr] * dataProb[state][n]

    return res


def initializeProb(state, otherState, dataProb, stringSeq):
    occurence = countOccurence(state, stringSeq)

    tempStr = str(state) + '|' + str(state)
    dataProb[tempStr] = countFollowedBy(state, state, stringSeq)/occurence

    tempStr = str(otherState) + '|' + str(state)
    dataProb[tempStr] = countFollowedBy(state, otherState, stringSeq)/occurence


def initializeMeas(measure, otherMeasure, dataProb, stateList):
    dataProb[measure] = [getMeasureProbability(measure, stateList, 0, dataProb)]
    dataProb[otherMeasure] = [getMeasureProbability(otherMeasure, stateList, 0, dataProb)]


def computeRes(resString, dataProb):
    tempS1, tempS2 = resString

    # get nth probability
    n = int(tempS1[-1])

    s1 = tempS1[0]
    s2 = tempS2[0]
    tempStr = s2 + '|' + s1

    res = (dataProb[tempStr]*dataProb[s1][n])/dataProb[s2][n]

    # if no truncation used:
    # temp = tempS1 + ' given ' + tempS2 + ' = ' + str(res)

    # for truncation like in hmm.out:
    res = int(res*10000)/10000
    temp = tempS1 + ' given ' + tempS2 + ' = ' + format("%.4f" % res)

    return temp
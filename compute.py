def getOtherState(state, stateList):
    other = ''
    if state == stateList[0]:
        other = stateList[1]
    else:
        other = stateList[0]
    return other

def countOccurence(state, stringSeq):
    count = 0
    for letter in stringSeq:
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

def initializeProb(state, otherState, stateProb, stringSeq):
    occurence = countOccurence(state, stringSeq)

    tempStr = str(state) + '|' + str(state)
    stateProb[tempStr] = [0, countFollowedBy(state, state, stringSeq)/occurence]



    tempStr = str(otherState) + '|' + str(state)
    stateProb[tempStr] = [0, countFollowedBy(state, otherState, stringSeq)/occurence]

def getMaxStateNeeded(resList):
    max = 0
    for res in resList:
        for pair in res:
            if max < int(min(pair)):
                max = int(min(pair))
    return max

def printStates(stateProb):
    for i in stateProb:
        print(i, stateProb[i])


def totalProbability(state, otherState, n, stateProb):
    result = 0

    tempStr = str(state) + '|' + str(state)

    result = stateProb[tempStr][n] * stateProb[state][n-1]

    tempStr = str(state) + '|' + str(otherState)

    result += stateProb[tempStr][n] * stateProb[otherState][n-1]

    return result
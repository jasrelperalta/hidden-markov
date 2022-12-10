import fileHandler
import compute

stateProb = {}

data = fileHandler.openFile('data/hmm.in')
# for i in data:
#     print(i)

numString, stringList, stateList, measureList, valList, resList = data

# maxIter = compute.getMaxStateNeeded(resList)
maxIter = 10

for stringSeq in stringList:
    stateProb = compute.getInitStates(stateList, stringSeq)

    # initialize
    for state in stateList:
        otherState = compute.getOtherState(state, stateList)
        compute.initializeProb(state, otherState, stateProb, stringSeq)

    for i in range(1, maxIter+1):
        for state in stateList:
            otherState = compute.getOtherState(state, stateList)
            stateProb[state].append(compute.totalProbability(state, otherState, i, stateProb))

    print('\n')
    compute.printStates(stateProb)
    break
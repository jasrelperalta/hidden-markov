import fileHandler
import compute

stateProb = {}

data = fileHandler.openFile('data/hmm.in')
# for i in data:
#     print(i)

numString, stringList, stateList, measureList, valList, resList = data

maxIter = compute.getMaxStateNeeded(resList)


for stringSeq in stringList:
    stateProb = compute.getInitStates(stateList, stringSeq)

    # initialize
    for state in stateList:
        otherState = compute.getOtherState(state, stateList)
        compute.initializeProb(state, otherState, stateProb, stringSeq)

    for state in stateList:
        otherState = compute.getOtherState(state, stateList)
        print(state, compute.totalProbability(state, otherState, 1, stateProb))

    print('\n')
    compute.printStates(stateProb)
    break
import fileHandler
import compute

dataProb = {}

data = fileHandler.openFile('data/hmm.in')
# for i in data:
#     print(i)

numString, stringList, stateList, measureList, valList, resList = data

maxIter = compute.getMaxStateNeeded(resList)
# maxIter = 5
resString = ''

for stringSeq in stringList:
    resString += stringSeq + '\n'
    
    # initialize dictionary that will hold all the values of states
    dataProb = compute.getInitStates(stateList, stringSeq)
    # combine the measure probabilities dictionary
    dataProb.update(compute.getMeasureDict(stateList, measureList, valList))

    # initialize
    for state in stateList:
        otherState = compute.getOtherState(state, stateList)
        compute.initializeProb(state, otherState, dataProb, stringSeq)

    for measure in measureList:
        otherMeasure = compute.getOtherState(measure, measureList)
        compute.initializeMeas(measure, otherMeasure, dataProb, stateList)


    for i in range(1, maxIter+1):
        for state in stateList:
            otherState = compute.getOtherState(state, stateList)
            dataProb[state].append(compute.totalProbability(state, otherState, i, dataProb))

        for measure in measureList:
            otherMeasure = compute.getOtherState(measure, measureList)
            dataProb[measure].append(compute.getMeasureProbability(measure, stateList, i, dataProb))

    
    # compute.printStates(dataProb)
    for res in resList:
        resString += compute.computeRes(res, dataProb) + '\n'


fileHandler.createOutput(resString)
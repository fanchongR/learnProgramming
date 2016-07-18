#os.chdir(r'C:\Users\Administrator\Desktop')

postingList=[['my', 'dog', 'has', 'flea', \
 'problems', 'help', 'please'],
 ['maybe', 'not', 'take', 'him', \
 'to', 'dog', 'park', 'stupid'],
 ['my', 'dalmation', 'is', 'so', 'cute', \
 'I', 'love', 'him'],
 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
 ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
 'to', 'stop', 'him'],
 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

classVec = [0,1,0,1,0,1]



def createVocabList(dataSet):
    uniqset = set([])
    for sample in dataSet:
        uniqset = uniqset | set(sample)
    return list(uniqset)

def setOfWords2Vec(uniqSet,sample):
    N = len(uniqSet)
    textVector = [0]*N
    for index in range(N):
        if uniqSet[index] in sample:textVector[index] = 1
    return textVector


# need numpy
def trainNBO(trainingSet,Labels):
    N = len(trainingSet)
    colN = len(trainingSet[0])
    condiProb0 = ones(colN)                      #
    condiProb1 = ones(colN)                    
    categoryRatio1 = sum(Labels)/N
    p0Denom = 2.0; p1Denom = 2.0                #
    
    for sampleNum in range(N):
        if Labels[sampleNum] == 0:
            condiProb0 += trainingSet[sampleNum]
            p0Denom += sum(trainingSet[sampleNum])
        else:
            condiProb1 += trainingSet[sampleNum]
            p1Denom += sum(trainingSet[sampleNum])
    condiProb0 = log(condiProb0/p0Denom)                #
    condiProb1 = log(condiProb1/p1Denom)
    return condiProb0,condiProb1,categoryRatio1
            

                


from numpy import *
myVocabList = createVocabList(postingList)
trainMat=[]
for sample in postingList:
    trainMat.append(setOfWords2Vec(myVocabList,sample))

p0V,p1V,pAb = trainNBO(trainMat,classVec)



def classifyNB(sampleVector,p0V,p1V,pAb):
    prob0 = sum(sampleVector * p0V) + log(1-pAb)              #
    prob1 = sum(sampleVector * p1V) + log(pAb)
    if prob0 > prob1:
        return 0
    else:
        return 1



classifyNB(setOfWords2Vec(myVocabList,['stupid', 'garbage']),p0V,p1V,pAb)

            
            

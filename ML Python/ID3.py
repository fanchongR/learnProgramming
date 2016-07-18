#os.chdir(r'C:\Users\Administrator\Desktop')

dataSet = [[1, 1, 'yes'],
 [1, 1, 'yes'],
 [1, 0, 'no'],
 [0, 1, 'no'],
 [0, 1, 'no']]
labels = ['no surfacing','flippers']



from math import log

def calcShannonEnt(dataset):
    N = len(dataset)
    labelscount={}
    for sample in dataset:
        label = sample[-1]
        labelscount.setdefault(label,0)
        labelscount[label]+=1
    Ent = 0
    for key in labelscount:
        prob = labelscount[key]/N
        Ent += -prob*log(prob,2)
    return Ent
    
def splitDataSet(dataset,axis,value):
    returndataset=[]
    for sample in dataset:
        if sample[axis] == value:
            sampleneed = sample[:axis]
            sampleneed.extend(sample[axis+1:])
            returndataset.append(sampleneed)
    return returndataset

def chooseBestFeatureToSplit(dataset):
    baseEntropy = calcShannonEnt(dataset)
    featureNumber = len(dataset[0]) - 1
    N = len(dataset)
    
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(featureNumber):
        featureList = [sample[i] for sample in dataset]
        levels = set( featureList )
        InfoGainNow = 0
        for level in levels:
            datasetNow = splitDataSet(dataset,i,level)
            InfoGainNow += len(datasetNow)/N * calcShannonEnt(datasetNow)
        InfoGainNow = baseEntropy - InfoGainNow
        if InfoGainNow > bestInfoGain:
            bestInfoGain = InfoGainNow
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    Count={}
    for vote in classList:
        Count.setdefault(vote,0)
        Count[vote]+=1
    return max(Count.items(), key=lambda x: x[1])[0]


def createTree(dataset,featurenames):
    labelsNow = [sample[-1] for sample in dataset]
    if len(set(labelsNow)) == 1:
        return labelsNow[0]
    elif len(dataset[0]) == 1:
        return majorityCnt(labelsNow)
    else:
        bestFeature = chooseBestFeatureToSplit(dataset)
        bestfeatureList = [sample[bestFeature] for sample in dataset]
        featurenamesNew = featurenames[:]
        del featurenamesNew[bestFeature]
        myTree={}
        myTree.setdefault(featurenames[bestFeature],{})
        for value in set(bestfeatureList):
            datasetSplit = splitDataSet(dataset,bestFeature,value)
            myTree[featurenames[bestFeature]][value] = createTree(datasetSplit,featurenamesNew)
        return myTree
    

def classify(treeModel,featurenames,testsample):
    import types
    
    feature = [key for key in treeModel][0]                   #key的拿出，注意要字符串而不是列表
    value = testsample[featurenames.index(feature)]
    if type(treeModel[feature][value]) == type('a'):           #type的判定
        return treeModel[feature][value]
    else:
        return classify(treeModel[feature][value],featurenames,testsample)



    
        
               


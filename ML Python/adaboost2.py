from numpy import *

def stumpclassify(dataset,feature,cutoff,inequal):
    N = shape(dataset)[0]
    labels = mat(ones((N,1)))

    values = dataset[:,feature]
    if inequal == 'greater':
        labels[values<cutoff] = -1
    else:
        labels[values>=cutoff] = -1
    return labels

def buildstump(dataset,ylabels,weights):
    N,featurenum = shape(dataset)
    
    stepnum = 20
    inequal = ['greater','less']
    
    baseclassify = {}
    besterror = inf
    bestpredictlabels = []
            
    for feature in range(featurenum):
        featurevalues = dataset[:,feature]
        start = float(featurevalues.min())
        end = float(featurevalues.max())
        steplength = (end - start)/stepnum
        for i in range(stepnum+1):
            cutoff = start + i * steplength
            for symbol in inequal:
                predictlabels = stumpclassify(dataset,feature,cutoff,symbol)
                errorlabels = mat(zeros((N,1)))
                errorlabels[predictlabels!=ylabels] = 1
                errornow = errorlabels.T * weights
                
                if errornow < besterror:
                    besterror = errornow
                    baseclassify['feature'] = feature
                    baseclassify['cutoff'] = cutoff
                    baseclassify['inequal'] = symbol
                    baseclassify['alpha'] = 0.5 * float(log((1-errornow)/max(errornow,1e-6)))  #
                    bestpredictlabels = predictlabels.copy()
    return baseclassify,besterror, bestpredictlabels
    

def adaboost(dataset,ylabels,iter=3):
    dataset = mat(dataset)
    ylabels = mat(ylabels).T
    N,featurenum = shape(dataset)
    
    weights = mat(ones((N,1)))
    weights = weights/sum(weights)
    classifyseq = []
    for iternum in range(iter):
        baseclassify,errorrate,predictlabels = buildstump(dataset,ylabels,weights)
        fixfactor = mat(ones((N,1)))
        fixfactor[predictlabels==ylabels] = -1 
        weights = multiply(weights,exp( baseclassify['alpha'] * fixfactor ))
        weights = weights/sum(weights)
        classifyseq.append(baseclassify)
        
    #    print weights
    #    print errorrate
        
    return classifyseq
 
trainx = []
for i in range(10):
      trainx.append([i])
trainy = [1,1,1,-1,-1,-1,1,1,1,-1]


from numpy import *

def calerror(dataset,ylabels,feature,cutoff):
    values = dataset[:,feature]
    lessyvalue = ylabels[values<cutoff]
    largeryvalue = ylabels[values>=cutoff]
    preless = lessyvalue.mean()
    pregreater = largeryvalue.mean()
    return sum( power(lessyvalue - preless,2) ) + sum( power(largeryvalue - pregreater,2) ),preless,pregreater
    
def baseregression(dataset,ylabels):
    besterror = inf
    stepnum = 20
    
    basereg = {}
    
    featurenum = shape(dataset)[1]
    for feature in range(featurenum):
        values = dataset[:,feature]
        start = float( values.min() )
        end = float( values.max() )  
        steplength = (end-start)/stepnum
        for i in range(stepnum+1):
            cutoff = start + i*steplength
            nowerror,preless,pregreater = calerror(dataset,ylabels,feature,cutoff)
            if nowerror < besterror:
                besterror = nowerror
                basereg['feature'] = feature
                basereg['cutoff'] = cutoff
                basereg['preless'] = preless
                basereg['pregreater'] = pregreater
    return basereg

def basetreepredict(basetree,dataset):
    values = dataset[:,basetree['feature']]
    
    N = shape(dataset)[0]
    result = mat(zeros((N,1)))
    result[values >= basetree['cutoff']] = basetree['pregreater']
    result[values < basetree['cutoff']] = basetree['preless']
    return result
    
def boostingregtrees(dataset,ylabels,ntree=6):
    dataset = mat(dataset)
    ylabels = mat(ylabels).T
    
    residuals = ylabels.copy()
    treeseq = []
    
    for i in range(ntree):
        basereg = baseregression(dataset,residuals)
        treeseq.append( basereg )
        residuals = residuals - basetreepredict(basereg,dataset)
    
    return treeseq
    
trainx = []
for i in range(1,11):
    trainx.append([i])
trainy = [5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05]


        
        
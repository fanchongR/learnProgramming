datMat = matrix([[ 1. , 2.1],
 [ 2. , 1.1],
 [ 1.3, 1. ],
 [ 1. , 1. ],
 [ 2. , 1. ]])

classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]

# 按照一定特征的一定阈值，做决策树桩分类
def stumpClassify(dataSet,dimen,threshVal,threshIneq):
    retlabels = ones((shape(dataSet)[0],1))
    if threshIneq == 'lt':
        retlabels[ dataSet[:,dimen]<=threshVal ] = -1
    else:
        retlabels[ dataSet[:,dimen]> threshVal ] = -1
    return retlabels
 
# 按照一定权重D，返回最佳决策树桩    
def buildStump(dataArr,classLabels,D):
    dataArr = mat(dataArr) ; classLabels = mat(classLabels).T
    m,n = dataArr.shape
    bestLabels = mat(zeros((m,1)));bestStump={};minErrorRate = inf
    stepNum = 10
    for i in range(n):
        Min = dataArr[:,i].min() ; Max = dataArr[:,i].max()
        stepSize = (Max - Min)/stepNum
        for j in range(0,stepNum+1):
            cutOff = Min + j * stepSize
            for Inequal in ['lt','gt']:
                predictValues = stumpClassify(dataArr,i,cutOff,Inequal)
                errorLabels = mat(zeros((m,1)))
                errorLabels[predictValues != classLabels] = 1
                errorRate = D.T * errorLabels
                if errorRate < minErrorRate:
                    minErrorRate = errorRate
                    bestLabels = predictValues.copy()             #
                    bestStump['dim'] = i
                    bestStump['thresh'] = cutOff
                    bestStump['ineq'] = Inequal
    return bestStump,minErrorRate,bestLabels

from math import *
def adaBoost(dataSet,classLabels,numIt=40):
    m,n = shape(dataSet)
    D = mat(ones((m,1)))/m 
    stumpArr = []
    aggClassEst = mat(zeros((m,1)))
    for i in range(numIt):
        bestStump,errorRate,retLabels = buildStump(dataSet,classLabels,D)
        alpha = float(log( (1-errorRate)/max(errorRate,1e-6))/2)        #
        bestStump['alpha'] = alpha
        stumpArr.append(bestStump)
        print('D',D.T)                                    #
        print('classEst:',retLabels.T)
        temp = multiply(-alpha*mat(classLabels).T,retLabels)       #
        D = multiply(exp(temp),D)                                  #
        D = D / sum(D)
        aggClassEst +=alpha*retLabels                      #
        print('aggClassEst',aggClassEst.T)
        aggErrors = multiply( sign(aggClassEst)!=mat(classLabels).T,ones((m,1)) )
        aggErrors = aggErrors.sum()/m
        print('total error:',aggErrors,'\n')
        if aggErrors == 0.0:break
    return stumpArr

adaBoost(datMat,classLabels,9)

def adaClassify(dataSet,classifySet):
    dataSet = mat(dataSet)
    m = shape(dataSet)[0]
    aggLabels = mat(zeros((m,1)))
    for classifier in classifySet:
        aggLabels += classifier['alpha'] * stumpClassify(dataSet,classifier['dim'],classifier['thresh'],classifier['ineq'])
    return sign(aggLabels)



dataSet

from numpy import *
def classifer(centerMat,sample):
    k = shape(centerMat)[0]
    minDistance = inf ; bestClass = -1
    for i in range(k):
        newDistance = sum(power(centerMat[i,:] - sample,2))
        if newDistance < minDistance:
            minDistance = newDistance
            bestClass = i+1
    return bestClass

#Labels 是列表
def classiferSet(centerMat,dataSet):
    Labels = []
    for sample in dataSet:
        Labels.append(classifer(centerMat,sample))
    return Labels    

def calCenters(dataSet,Labels,k):
    n = shape(dataSet)[1]
    Labels = array(Labels)
    centers = mat(zeros((k,n)))
    for i in range(1,k+1):
        subSet = dataSet[Labels == i,:]
        centers[i-1,:] = mean(subSet,axis=0)
    return centers


def kmeans(dataSet,k,ops=1e-4):
    m = shape(dataSet)[0]
    
    import random
    initiaCentersIndex = random.sample(range(0,m),k)
    centerMat = dataSet[initiaCentersIndex,:]

    for i in range(100):
        Labels = classiferSet(centerMat,dataSet)
        newCenterMat = calCenters(dataSet,Labels,k)
        if sqrt(sum(power(newCenterMat - centerMat,2))) < ops:
            return Labels,newCenterMat
        centerMat = newCenterMat

        


        
    
    

        
        
        
    

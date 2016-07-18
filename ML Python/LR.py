from numpy import *

def sigmoid(x):
    return 1/(1+exp(-x))

def logisticregression(trainx,trainy,opts):
    alpha = opts['alpha']
    maxiter = opts['maxiter']
    samplenum,featurenum = shape(trainx)
    weights = mat(ones((featurenum,1)))
    
    for k in range(maxiter):
      
        errors = trainy - sigmoid(trainx*weights)
        weights = weights + alpha * trainx.transpose() * errors
        
    return weights
    

def predict_lr(weights,samples):
    return sigmoid(samples*weights)
    


    
###########
file = open('/Users/FC/python/iris')
featurename = file.readline()

trainx = []
trainy = []
for line in file:
    temp = line.rstrip().split('\t')
    temp2 = [1.0 , float(temp[2]),float(temp[3])]
    trainx.append(temp2)

trainx = mat(trainx[0:100])
trainy = [1 for x in range(50)] + [0 for x in range(50)]
trainy = mat(trainy).T

opts={}
opts['maxiter'] = 1000
opts['alpha'] = 0.01
weights = logisticregression(trainx,trainy,opts)
        
    
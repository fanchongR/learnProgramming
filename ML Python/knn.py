#knn

from numpy import *
import operator


group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
labels = ['A','A','B','B']


def knn(x,samples,labels,k):
    N = samples.shape[0]
    diff = tile(x,(N,1)) - samples
    diff = diff**2
    distances = sum(diff,axis=1)
    orders = distances.argsort()

    labelscount = {}
    for i in range(k):
        labelnow = labels[where(orders == i)[0][0]]
        labelscount.setdefault(labelnow,0)
        labelscount[labelnow]+=1

    return max(labelscount.items(), key=lambda x: x[1])[0]


    
        
    
    
    

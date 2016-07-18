from numpy import *
import random


# X0 = 1
def perceptron(X,Y,lamda=0.05,iter=100):
    for i in  range(len(X)):
        X[i].insert(0,1)
    X = mat(X) ; Y = mat(Y).T
    N = shape(X)[1]
    w = mat(zeros((N,1)))
#    for i in range(N):
#        w[i,0] = random.random()
        
    for itern in range(iter):
        for i in range(N):
            labelnow =  sign(X[i,:] * w)
            if Y[i,:] != labelnow:w = w + lamda*Y[i,0]*X[i,:].T
    return w
    
    
X = [[3,3],[4,3],[1,1]]
Y = [1,1,-1]

perceptron(X,Y,lamda=1,iter=8)
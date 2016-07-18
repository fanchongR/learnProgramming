# -*- coding: utf-8 -*-
#径向基函数神经网络，泛化能力很差，不知哪里写错了

from numpy import *
import random

def nn(Xo,Yo,hidden=10,sigma=5):
    X = mat(Xo) ; Y = mat(Yo).T       #notice to fix
    M,N = shape(X)
#   w1 = row_stack((mean(X[:25,:],axis=0),mean(X[25:50,:],axis=0),mean(X[50:75,:],axis=0),mean(X[75:,:],axis=0)))    ####
    w1index = []
    for i in range(hidden):
        j = random.randint(0,M-1)
        w1index.append(j)
    w1 = X[w1index,:]
    
    z = createHiddenNode(X,w1,sigma)
    z = column_stack((z,ones((M,1))))
    w2 = linalg.pinv(z) * Y
    return w1,w2
    
def tanh(x):
    return 1/(1+exp(-x))
    #return (exp(x)-exp(-x))/(exp(x)+exp(-x))
    
def Gaussian(x,w,sigma=0.1):
    return exp( - sum(power((x-w),2)) /(2 * sigma**2))
def createHiddenNode(X,w1,sigma):
    M = shape(X)[0]
    Mw = shape(w1)[0]
    z = mat(zeros((M,Mw)))
    for i in range(M):
        for j in range(Mw):
            z[i,j] = Gaussian(X[i,:],w1[j,:],sigma)
    return z
    

def predict(Xo,w1,w2,sigma=0.1):
    M = shape(Xo)[0]
    z = createHiddenNode(Xo,w1,sigma)
    z = column_stack((z,ones((M,1))))
    Y = z*w2
    return Y



w1,w2=nn(Xo,Yo)
predict(Xo,w1,w2)


############################### scale
Xo = mat(Xo)
for i in range(shape(Xo)[1]):
    Xo[:,i] = (Xo[:,i] - mean(Xo[:,i]))/var(Xo[:,i])

mean(Xo[:50,:],axis=0)
#matrix([[-1.14065923,  1.44998435, -0.67253828, -1.70775828]])
mean(Xo[50:,:],axis=0)
#matrix([[ 1.14065923, -1.44998435,  0.67253828,  1.70775828]])
###############################
w1,w2 = nn(Xo,Yo,iter=3000)
result = predict(Xo,w1,w2)
prelabels = []
for i in range(shape(result)[0]):
    if result[i,0] > 0.5:prelabels.append(1)
    else:prelabels.append(0)
print mean(mat(prelabels) == mat(Yo))



import sys
dataset = []
file = open('/Users/FC/python/iris')
file.readline()
for line in file:
    line = line.strip().split()
    line = [ float(num) for num in line[:-1]]
    dataset.append(line)
Xo = dataset[:100]
Yo = [0] * 50 + [1] * 50


    
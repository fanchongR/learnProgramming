from numpy import *
import random

def nn(Xo,Yo,hidden=5,lamda=0.1,iter=1000):
    X = mat(Xo) ; Y = mat(Yo).T       #notice to fix
    M,N = shape(X)
    X = column_stack((X,ones((M,1))))
    w1 = mat(ones((N+1,hidden)))
    w2 = mat(ones((hidden+1,shape(Y)[1])))
    
    for i in range(shape(w1)[0]):
        for j in range(shape(w1)[1]):
            w1[i,j] = random.random()
    for i in range(shape(w2)[0]):
        for j in range(shape(w2)[1]):
            w2[i,j] = random.random()
    
    
    for niter in range(iter):
        a = X*w1
        z = tanh(a)
        z = column_stack((z,ones((M,1))))
        predY = sigmoid(z*w2)              #
        delta2 = predY - Y
        delta1 = multiply((1-power(z,2)),delta2 * (w2.T))
        
        w1 += -lamda * X.T * delta1[:,:-1]
        w2 += -lamda * z.T * delta2
    return w1,w2
    
def tanh(x):
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def sigmoid(x):
    return 1/(1+exp(-x))

def predict(Xo,w1,w2):
    X = mat(Xo)         #notice to fix 
    M = shape(X)[0]
    X = column_stack((X,ones((M,1))))
    a = X*w1
    z = tanh(a)
    z = column_stack((z,ones((M,1))))
    Y = z*w2
    return sigmoid(Y) 

    


Xo = [[3,3],[4,3],[1,1]]
Xo = [3,4,1]
Yo = [1,1,0]
########
Xo = [1,2,3,5,4.3,-1,-10,-2,-3,-4.4]
Xo = [[i] for i in Xo]
Yo = [1,1,1,1,1,0,0,0,0,0]
########
Xo = []
Yo = []
for i in range(1000):
    num = random.random()
    Xo.append([num])
    if num > 0.6:Yo.append(1)
    else:Yo.append(0)



############################### scale
Xo = mat(Xo)
for i in range(shape(Xo)[1]):
    Xo[:,i] = (Xo[:,i] - mean(Xo[:,i]))/var(Xo[:,i])
    
    
w1,w2 = nn(Xo,Yo,iter=1000)
predict(Xo,w1,w2)
###############################
Xo = mat(Xo)
for i in range(shape(Xo)[1]):
    Xo[:,i] = (Xo[:,i] - mean(Xo[:,i]))/var(Xo[:,i])
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


    


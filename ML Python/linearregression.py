# -*- coding: utf-8 -*-
from numpy import *

def linearreg(X,Y):
    X = mat(X) ; Y = mat(Y).T
    xTx = X.T*X
    if linalg.det(xTx) == 0.0:
        return 
    return xTx.I * (X.T*Y)          #第一维是常数项 即假设x0=1
    
    
def lwlr(testsample,X,Y,k = 1.0):      #局部线性加权回归
    X = mat(X) ; Y = mat(Y).T
    m = shape(X)[0]
    W = mat(eye(m))
    
    for i in range(m):
        diff = testsample - X[i,:]
        W[i,i] = exp( (diff*diff.T)/(-2.0*k**2) )
    
    return (X.T*W.X).I *X.T * W*Y
    
def ridgereg(X,Y,lamda = 0.2):    #岭回归
    X = mat(X) ; Y =mat(Y).T
    m = shape(X)[1]
    temp = X.T*X + lamda*mat(eye(m))
    if linalg.det(temp) == 0:return 
    ws = temp.I * X.T * Y
    return ws
    

    
    
    
    
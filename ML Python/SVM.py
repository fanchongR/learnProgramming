from numpy import *
import random

def selectJrand(i,m):
    j = i
    while j==i:
        j = int(random.uniform(0,m))
    return j
    
def clipAlpha(aj,H,L):
    if aj > H:aj = H
    if aj < L:aj = L
    return aj
    

def smoSimple(data,label,C,toler,maxIter):
    data = mat(data);label = mat(label).T
    m,n = shape(data)
    b = 0; alphas = mat(zeros((m,1)))
    iter = 0
    
    while iter < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,label).T*(data*data[i,:].T)) + b
            Ei = fXi - float(label[i])
            
            if (label[i] * Ei < -toler and alphas[i] < C) or (label[i] * Ei > toler and alphas[i] > 0):
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,label).T*(data*data[j,:].T)) + b
                Ej = fXj - float(label[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if label[i] != label[j]:
                    L = max(0,alphas[j]-alphas[i])
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L == H:continue                           ###
                eta = 2.0 * data[i,:] * data[j,:].T - data[i,:]*data[i,:].T - data[j,:]*data[j,:].T
                if eta >= 0:continue                           ###
                alphas[j] -= label[j]*(Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if abs(alphas[j] - alphaJold) < 0.00001:continue      ###
                alphas[i] += label[i]*label[j]*(alphaJold-alphas[j])
                
                b1 = b - Ei - label[i] * (alphas[i]-alphaIold)*data[i,:]*data[i,:].T - label[j]*(alphas[j]-alphaJold)*data[i,:]*data[j,:].T
                b2 = b - Ej - label[i] * (alphas[i]-alphaIold)*data[i,:]*data[j,:].T - label[j]*(alphas[j]-alphaJold)*data[j,:]*data[j,:].T
                if alphas[i] > 0 and alphas[i] < C:b = b1
                elif alphas[j] > 0 and alphas[j] < C:b = b2
                else:b = (b1 + b2)/2
                alphaPairsChanged += 1
                
        if alphaPairsChanged == 0:iter += 1
        else: iter = 0
    return b,alphas
    
    
    
    
#######################################################

class optStruct:
    def __init__(self,dataMat,labels,C,toler):
        self.X = dataMat
        self.label = labels
        self.C = C
        self.tol = toler
        self.m = shape(dataMat)[0]
        self.alphas = mat(zeros((self.m,1)))
        self.b = 0
        self.eCache = mat(zeros((self.m,2)))
    
def calcEk(oS,k):
    fXk = float(multiply(oS.alphas,oS.label).T * (oS.X*oS.X[k,:].T)) + oS.b
    Ek = fXk - float(oS.label[k])
    return Ek
        
def selectJ(i,oS,Ei):
    maxK = -1 ; maxDeltaE = 0 ; Ej = 0
    oS.eCache[i] = [1,Ei]
    validEcacheList = nonzero(oS.eCache[:,0].A)[0]
    if len(validEcacheList) > 1:
        for k in validEcacheList:
            if k == i:continue
            Ek = calcEk(oS,k)
            deltaE = abs(Ei - Ek)
            if deltaE > maxDeltaE:
                maxK = k ; maxDeltaE = deltaE ; Ej = Ek
        return maxK,Ej
    else:
        j = selectJrand(i,oS.m)
        Ej = calcEk(oS,j)
        return j,Ej
        
def updateEk(oS,k):
    Ek = calcEk(oS,k)
    oS.eCache[k] = [1,Ek]
    

def innerL(i,oS):
    Ei = calcEk(oS,i)
    if (oS.label[i]*Ei < -oS.tol and oS.alphas[i] < oS.C) or (oS.label[i]*Ei > oS.tol and oS.alphas[i] > 0):
        j,Ej = selectJ(i,oS,Ei)           ###
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if oS.label[i] != oS.label[j]:
            L = max(0,oS.alphas[j]-oS.alphas[i])
            H = min(oS.C,oS.C+oS.alphas[j]-oS.alphas[i])
        else:
            L = max(0,oS.alphas[j]+oS.alphas[i]-oS.C)
            H = min(oS.C,oS.alphas[j]+oS.alphas[i])
        if L == H:return 0
        eta = 2.0 * oS.X[i,:]*oS.X[j,:].T - oS.X[i,:]*oS.X[i,:].T - oS.X[j,:]*oS.X[j,:].T
        if eta >= 0:return 0
        
        oS.alphas[j] -= oS.label[j]*(Ei-Ej)/eta
        oS.alphas[j] = clipAlpha(oS.alphas[j],H,L)
        updateEk(oS,j)                  ###
        if abs(oS.alphas[j] - alphaJold) < 0.00001: return 0
        oS.alphas[i] += oS.label[j]*oS.label[i]*(alphaJold-oS.alphas[j])
        updateEk(oS,i)                  ###
        
        b1 = oS.b - Ei - oS.label[i] * (oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[i,:].T - oS.label[j]*(oS.alphas[j]-alphaJold)*oS.X[i,:]*oS.X[j,:].T
        b2 = oS.b - Ej - oS.label[i] * (oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[j,:].T - oS.label[j]*(oS.alphas[j]-alphaJold)*oS.X[j,:]*oS.X[j,:].T
        if oS.alphas[i] > 0 and oS.alphas[i] < oS.C:oS.b = b1
        elif oS.alphas[j] > 0 and oS.alphas[j] < oS.C:oS.b = b2
        else:oS.b = (b1 + b2)/2.0
        return 1
    else:return 0   
    
def smoP(data,label,C,toler,maxIter,kTup=('lin',0)):
    oS = optStruct(mat(data),mat(label).T,C,toler)
    iter = 0
    entireSet = True ; alphapairsChanged = 0
    while iter < maxIter and (alphapairsChanged > 0 or entireSet):
        alphapairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphapairsChanged += innerL(i,oS)
            iter += 1
        else:
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphapairsChanged += innerL(i,oS)
            iter += 1
        if entireSet: entireSet = False
        elif alphapairsChanged == 0: entireSet = True
    return oS.b,oS.alphas
    
    
                

    
    
    
        
        
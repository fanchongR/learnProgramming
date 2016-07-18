from numpy import *

#二切分数 大于在左边
def binSplitDataSet(dataSet,feature,value):
    left = dataSet[array((dataSet[:,feature] > value).T)[0],:]            
    right =  dataSet[ array((dataSet[:,feature] <= value).T)[0],: ]
    return left,right

# leafType给出了建立叶结点的函数 errType代表误差计算函数 ops是所需的其他参数
def createTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val = chooseBestSplit(dataSet,leafType,errType,ops)
    if feat == None:return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet,rSet = binSplitDataSet(dataSet,feat,val)
    retTree['left'] = createTree(lSet,leafType,errType,ops)
    retTree['right'] = createTree(rSet,leafType,errType,ops)
    return retTree

#########################################
testMat=mat(eye(4))
binSplitDataSet(testMat,1,0.5)

#CART
def regLeaf(dataSet):
    return mean(dataSet[:,-1])
def regErr(dataSet):
    return var(dataSet[:,-1]) * shape(dataSet)[0]

#ops是允许的误差下降值 和 接受的最小样本数
def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS = ops[0] ; tolN = ops[1]
    if len( set(dataSet[:,-1].T.tolist()[0]) ) == 1:
        return None,leafType(dataSet)

    m,n = shape(dataSet)
    S = errType(dataSet)
    bestS = inf ; bestIndex = 0 ; bestValue = 0
    for splitFeature in range(n-1):
        for splitValue in set(dataSet[:,splitFeature].T.tolist()[0]):               #修改过
            mat0,mat1 = binSplitDataSet(dataSet,splitFeature,splitValue)
            if shape(mat0)[0]<tolN or shape(mat1)[0]<tolN:continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestS = newS
                bestIndex = splitFeature
                bestValue = splitValue
    if S - bestS < tolS:
        return None,leafType(dataSet)
    mat0,mat1 = binSplitDataSet(dataSet,bestIndex,bestValue)
    if shape(mat0)[0]<tolN or shape(mat1)[0]<tolN:
        return None,leafType(dataSet)
    return bestIndex,bestValue


#ops事实上对数据数量级（其实是误差数量级）很敏感。如果数据集数量级大了，就很容易过拟合，
#而通过不断调整参数ops，也没有什么好的标准说我们需要这样的结果。所以预剪枝是有局限性的。
#这时候需要后剪枝

def istree(treemodel):
    import types
    return type(treemodel) == type({})
def getMean(tree):
    if istree(tree['left']):tree['left']=getMeat(tree['left'])
    if istree(tree['right']):tree['right']=getMean(tree['right'])
    return (tree['left'] + tree['right'])/2

def prune(tree,testData):
    if shape(testData)[0] == 0:           #测试集为空，则无法剪枝,对树进行塌陷处理
        return getMean(tree)
    if istree(tree['left']) or istree(tree['right']):
        lset,rset = binSplitDataSet(testData,tree['spInd'],tree['spVal'])
    if istree(tree['left']):
        tree['left'] = prune(tree['left'],lset)
    if istree(tree['right']):
        tree['right'] = prune(tree['right'],rset)

    if not ( istree(tree['left']) or istree(tree['right']) ):
        lset,rset = binSplitDataSet(testData,tree['spInd'],tree['spVal'])
        errorNotMerge = sum( power(lset[:,-1] - tree['left'],2) ) +\
                        sum( power(rset[:,-1] - tree['right'],2) )
        treeMean = (tree['left'] + tree['right'])/2
        errorMerge = sum( power(testData[:,-1] - treeMean,2) )
        if errorMerge < errorNotMerge:
            return treeMean
        else:
            return tree
    return tree
        
        
        
###模型树，叶结点是分段线性函数
###比回归树解释性更好，有更高的预测精确度
def linearSolve(dataSet):
    m,n = shape(dataSet)
    X = mat(ones((m,n))) ; Y = mat(ones((m,1)))
    X[:,1:n] = dataSet[:,:-1] ; Y = dataSet[:,-1]
    xTx = X.T*X
    if linalg.det(xTx) == 0:
        raise NameError('This matrix is singular, cannot do inverse,\ntry increasing the second value of ops')
    ws = xTx.I * (X.T * Y)
    return ws,X,Y

# 负责生成叶节点模型
def modelLeaf(dataSet):
    ws,X,Y = linearSolve(dataSet)
    return ws

#计算给定数据集的误差
def modelErr(dataSet):
    ws,X,Y = linearSolve(dataSet)
    predY = X * ws
    return sum(power(Y - predY,2))


createTree(dataSet,modelLeaf,modelErr,(1,10))


############预测
def regTreeEval(model,inDat):
    return float(model)

def modelTreeEval(model,inDat):
    n = shape(inDat)[1]
    X = mat(ones((1,n+1)))
    X[:,1:] = inDat
    return float(X*model)

import types
def treeForeCast(tree,inData,modelEval=regTreeEval):
    if type(tree) = type({}):
        if inData[tree['spInd']] > tree['spVal']:
            return treeForeCast(tree['left'],inData,modelEval)
        else:
            return treeForeCast(tree['right'],inData,modelEval)
    return modelEval(tree,inData)

def createForeCast(tree,testData,modelEval=regTreeEval):
    predY = []
    for sample in testData:
        predY.append( treeForeCast(tree,sample,modelEval) )
    return mat(predY).T

    
    
    








    
    
    

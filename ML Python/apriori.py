dataset = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
D = list(map(set,dataset))

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])      #python不能创建只包含一个整数的集合
    C1.sort()
    return list(map(frozenset,C1))         #frozenset可以作为字典的键值

def scanD(D,CK,minSupport):
    freSubset = {}
    for temp in CK:
        for transaction in D:
            if temp.issubset(transaction):
                freSubset.setdefault(temp,0)
                freSubset[temp] += 1
    N = len(D)
    retList = [] ; supportData = {}
    for key in freSubset:
        supportnow = freSubset[key]/N
        if supportnow >= minSupport:
            retList.append(key)
            supportData[key] = supportnow
    return retList,supportData

C1 = createC1(dataset)
scanD(D,C1,0.5)

#Lk k-1项的频繁项集，构造k项的频繁项集
def aprioriGen(Lk,k):
    retList = []
    N = len(Lk)
    for i in range(N):
        for j in range(i+1,N):
            L1 = list(Lk[i])[:k-2] ; L2 = list(Lk[j])[:k-2]     #
            L1.sort() ; L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet,minSupport=0.5):
    Cl = createC1(dataSet)
    D = list(map(set,dataSet))
    Ll,supportData = scanD(D,Cl,minSupport)
    L = [Ll]
    k = 2
    while len(L[k-2])>0:
        Ck = aprioriGen(L[k-2],k)
        Lk,tempData = scanD(D,Ck,minSupport)
        supportData.update(tempData)
        L.append(Lk)
        k +=1
    return L,supportData


############################RULES

#freqSet 具有一定项目数的频繁项集L[i]的元素    H1 freqSet的元素的fronzenset列表
def generateRules(L,supportData,minConf=0.7):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i>1:
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

# 计算brl：freqSet - H各个元素的关联规则。 返回：关联规则后项集合的列表
def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf >= minConf:
            print(freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

#频繁项集freqSet　中得到的关联规则
def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    m = len(H[0])
    if len(freqSet)>m+1:
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet,Hmp1,supportData,brl,minConf)
            
    
    
    
        
    
    
    
    




        
    
    
    

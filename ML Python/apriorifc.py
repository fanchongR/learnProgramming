dataset = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])       #python不能创建只包含一个整数的集合
    C1.sort()
    return list(map(frozenset,C1))       #frozenset可以作为字典的键值

def scanD(Ck,D,minSupport=0.5):
    freData = {}
    for freset in Ck:
        for transaction in D:
            if freset.issubset(transaction):
                freData.setdefault(freset,0)
                freData[freset] += 1

    Lk = []
    supportData = {}
    N = len(D)
    for key in freData:
        temp = freData[key]/N
        if temp >= minSupport:
            supportData[key] = temp
            Lk.append(key)
    return Lk,supportData

#Lk k-1项的频繁项集，构造k项的频繁项集
def aprioriGen(Lk,k):
    N = len(Lk)
    Ck = []
    for i in range(N):
        for j in range(i+1,N):
            L1 = list(Lk[i])[:k-2]                   #
            L2 = list(Lk[j])[:k-2]
            if L1.sort() == L2.sort():
                Ck.append(Lk[i] | Lk[j])
    return Ck

def apriori(dataSet,minSupport=0.5):
    D = list(map(set,dataSet))
    C1 = createC1(dataSet)
    L1,supportData = scanD(C1,D,minSupport)
    L = [L1]
    k = 2
    while len(L[k-2]) >0:
        Ck = aprioriGen(L[k-2],k)
        Lk,tempData = scanD(Ck,D,minSupport)
        L.append(Lk)
        supportData.update(tempData)
        k += 1
    return L,supportData


        
############################RULES

#freqSet 具有一定项目数的频繁项集L[i]的元素    H1 freqSet的元素的fronzenset列表
def generateRules(L,supportData,minConf=0.7):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet,H,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H,supportData,bigRuleList,minConf)
    return bigRuleList

        
# 计算brl：freqSet - H --> H各个关联规则(H是freqset确定项数的子集列表)。
# 返回：关联规则后项集合的列表
def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    seconds = []
    for item in H:
        conf = supportData[freqSet]/supportData[freqSet-item]
        if conf >= minConf:
            brl.append((freqSet-item,item,conf))
            print(freqSet-item,'-->',item,'conf:',conf)
            seconds.append(item)
    return seconds


#频繁项集freqSet　中得到的关联规则
def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    m = len(H[0])
    if len(freqSet)>m+1:
        Hmp = aprioriGen(H,m+1)
        Hmp = calcConf(freqSet,Hmp,supportData,brl,minConf)
        if len(Hmp)>1:
            rulesFromConseq(freqSet,Hmp,supportData,brl,minConf)
        
        
        
    


    
                
    
    

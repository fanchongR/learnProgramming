import time
import random
import math

people = [('Seymour','BOS'),
 ('Franny','DAL'),
 ('Zooey','CAK'),
 ('Walt','MIA'),
 ('Buddy','ORD'),
 ('Les','OMA')]
destination='LGA'



flights={}
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip( ).split(',')
    flights.setdefault((origin,dest),[])
    flights[(origin,dest)].append((depart,arrive,int(price)))
def getminutes(t):
 x=time.strptime(t,'%H:%M')
 return x[3]*60+x[4]

#用一个列表描述题解
#[1,4,3,2,7,3,6,3,2,4,5,3]

#题解的解释
def printschedule(r):
 for d in range(len(r)/2):
 name=people[d][0]
 origin=people[d][1]
 out=flights[(origin,destination)][r[d]]
 ret=flights[(destination,origin)][r[d+1]]
 print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,
 out[0],out[1],out[2],
 ret[0],ret[1],ret[2])

#成本函数是优化算法解决问题的关键，也是最难确定的。算法的目标，就是要寻找一组输入，使成本函数
#的返回结果最小化。成本函数返回的值越大，方案越差



#成本函数
def schedulecost(sol):
 totalprice=0
 latestarrival=0
 earliestdep=24*60
 for d in range(len(sol)/2):
 origin=people[d][1]
 outbound=flights[(origin,destination)][int(sol[d])]
 returnf=flights[(destination,origin)][int(sol[d+1])]
 totalprice+=outbound[2]
 totalprice+=returnf[2]

 if latestarrival<getminutes(outbound[1]): latestarrival=getminutes(outbound[1])
 if earliestdep>getminutes(returnf[0]): earliestdep=getminutes(returnf[0])

 totalwait=0
 for d in range(len(sol)/2):
 origin=people[d][1]
 outbound=flights[(origin,destination)][int(sol[d])]
 returnf=flights[(destination,origin)][int(sol[d+1])]
 totalwait+=latestarrival-getminutes(outbound[1])
 totalwait+=getminutes(returnf[0])-earliestdep
 if latestarrival>earliestdep: totalprice+=50
 return totalprice+totalwait



#########随机搜索法

#Domain 是二元组构成的列表，指定了题解中每个变量的最大最小值，是所有可能题解的集合
#如 [(0, 9), (0, 9), (0, 9), (0, 9), (0, 9), (0, 9)...]
#costf  是成本函数

def randomoptimize(domain,costf):
 best=999999999
 bestr=None
 for i in range(1000):
 # Create a random solution
 r=[random.randint(domain[i][0],domain[i][1])
 for i in range(len(domain))]
 cost=costf(r)
 # Compare it to the best one so far
 if cost<best:
 best=cost
 bestr=r
 return r

domain=[(0,9)]*(len(people)*2)
s=randomoptimize(domain,schedulecost)


###########爬山法 缺点是会找到局部最小值

def hillclimb(domain,costf):
    sol=[random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
    while 1:
        neighbors = []
        for j in range(len(domain)):
            if sol[j] > domain[j][0]:
                neighbors.append(sol[:j]+[sol[j]-1]+sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[:j]+[sol[j]+1]+sol[j+1:])
        current = costf(sol)
        best = current
        for j in range(len(neighbors)):
            costnow = costf(neighbors[j])
            if costnow < best:
                best = costnow
                sol = neighbors[j]

        if best == current:
            break
    return sol


###########模拟退火
#模拟退火算法之所以管用，不仅因为它总是会接受一个更优的解，而且还因为它在退火过程的开始阶段
#会接受表现较差的解，而随着退火过程的不断进行，算法越来越不可能接受较差的解

def annealing(domain,costf,T=10000,cool=0.95,step=1):
    #随机初始化值
    vec=[float(random.randint(domain[i][0],domain[i][1])) for i in range(len(domain))]

    while T>0.1:
        i = random.randint(0,len(domain)-1)
        dir = random.randint(-step,step)
        vecb = vec[:]
        vecb[i] += dir
        if vecb[i] < domain[i][0]:vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:vecb[i] = domain[i][1]
        ea = costf(vec)
        eb = costf(vecb)
        if eb < ea or random.random() < pow(math.e,-(eb-ea)/T):
            vec = vecb
        T = T*cool        #降低温度
    return vec
            
        
##########函数求极少值的模拟退火
def annealing(costf,T=10000,cool=0.95,step=0.1):
	x0 = random.randint(0,10)
	while T >0.1:
		dir = random.sample([-step,step],1)
		x1 = x0
		x1 += dir[0]
		x0_cost = costf(x0)
		x1_cost = costf(x1)
		if x1_cost < x0_cost or random.random()<pow(math.e,-(x1_cost-x0_cost)/T):
			x0 = x1
		T = T*cool
	return x0

##########遗传算法
#精英选拔：当前种群中最优的解传入下一代
#变异：对既有解进行随机的微调
#交叉：选择两个最优解，进行某种结合

#popsize 种群大小 elite精英比例 mutprob变异而不是配对的概率 maxiter迭代次数
def geneticalgorithms(domain,costf,popsize=50,step=1,mutprob=0.2,elite=0.2,maxiter=100):
    def mutate(vec):
        i = random.randint(0,len(domain)-1)
        if random.random()<0.5 and vec[i]>domain[i][0]:
            return vec[:i]+[vec[i]-step]+vec[i+1:]
        elif vec[i]<domain[i][1]:
            return vec[:i]+[vec[i]+step]+vec[i+1:]

    def crossover(vec1,vec2):
        i = random.randint(1,len(domain)-2)
        return vec1[:i]+vec2[i:]

    pop = []
    for i in range(popsize):
        vec = [ random.randint(domain[i][0],domain[i][1]) for i in range(len(domain)) ]
        pop.append(vec)
    topelite = int(elite * popsize)


    for i in range(maxiter):
        scores = [(costf(vec),vec) for vec in pop]
        scores.sort()
        ranking = [item[1] for item in scores]
        pop = ranking[:topelite]

        while len(pop)<popsize:
        if random.random()<mutprob:
            index = random.randint(0,topelite-1)
            pop.append(mutate(pop[index]))
        else:
            index1 = random.randint(0,topelite-1)
            index2 = random.randint(0,topelite-1)
            pop.append( crossover(pop[index1],pop[index2]) )

    return scores[0][1]
            
            
#大多数优化算法都有赖于一个事实：最优解应该接近于其他优解。如果不这样，没有一种优化方法一定
#会比随机搜索好
        
        
        
        


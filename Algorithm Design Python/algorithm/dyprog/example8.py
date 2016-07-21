# -*- coding:utf-8 -*-
#P209

if __name__ == '__main__':
    def costOfProduction(a):
        if a == 0:
            return 0.0
        else:
            return float(a+3)
    def costOfStore(a):
        return float(0.5 * a)
    
    need = [0,2,3,2,4]
    max_production = 6
    max_store = 3
    
    def optimalDecision(decisions,status,costOfProduction,costOfStore,optimal_cost_next,need_now):
        optimal_cost = float('inf')
        optimal_decision = None
        for decision in decisions:
            cost_now = costOfProduction(decision) + costOfStore(status) + optimal_cost_next[status + decision - need_now][1]
            if cost_now < optimal_cost:
                optimal_cost = cost_now
                optimal_decision = decision
        return optimal_decision,optimal_cost
    
    x = [None,{},{},{},{},{}]  #状态 ->(最优生产量,最小花费)
    x[-1][0] = (0,0)
        
    for step in range(1,5)[::-1]:
        for status in range(max_store+1):
            if step == 1 and status != 0:continue
            decisions = []
            for decision in range(max_production+1):
                if step == 4 and decision+status - need[step] != 0:continue 
                if decision + status - need[step] > max_store or decision + status - need[step] < 0:continue
                decisions.append(decision)

            x[step][status] = optimalDecision(decisions,status,costOfProduction,costOfStore,x[step+1],need[step])
                
    for i in x:print(i)          
    status = 0
    optimal_decisions = [-1] * 5
    for i in range(1,5):
        optimal_decisions[i] = x[i][status][0]
        status = optimal_decisions[i] + status - need[i]
    print(optimal_decisions)
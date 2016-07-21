# -*- coding:utf-8 -*-
#P209

if __name__ == '__main__':
    profit = [5,4.5,4,3.75,3,2.5]
    fix_cost = [0.5,1,1.5,2,2.5,3]
    update_cost = [0.5,1.5,2.2,2.5,3,3.5]
    
    def optimalDecision(status,profit,costOfFix,costOfUpdate,optimal_profit_next):
        optimal_profit = -float('inf')
        optimal_decision = None
        for decision in [0,1]:
            if decision == 0:
                profit_now = profit[status] - costOfFix[status] + optimal_profit_next[status + 1][1]
            elif decision == 1:
                profit_now = profit[0] - costOfFix[0] - costOfUpdate[status] + optimal_profit_next[1][1]
            if profit_now > optimal_profit:
                optimal_profit = profit_now
                optimal_decision = decision
        return optimal_decision,optimal_profit
    
    x = [None,{},{},{},{},{},{}]  #״̬ ->(����������,��С����)
    for status in range(7):x[-1][status] = (0,0)
        
    for step in range(1,6)[::-1]:
        for status in range(0,6):
            if step != 1 and status == 0:continue
            if status < step:
                x[step][status] = optimalDecision(status,profit,fix_cost,update_cost,x[step+1])
                
    for i in x:print(i)          
    status = 0
    optimal_decisions = [-1] * 6
    for i in range(1,6):
        optimal_decisions[i] = x[i][status][0]
        if optimal_decisions[i] == 0:
            status += 1
        elif optimal_decisions[i] == 1:
            status = 1

    print(optimal_decisions)
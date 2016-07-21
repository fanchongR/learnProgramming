# -*- coding:utf-8 -*-
if __name__ == '__main__':
    def profit1(a):return 4*a
    def profit2(a):return 5*a
    def profit3(a):return 6*a
    def profit4(a):return 0
    profitList = [profit1,profit2,profit3,profit4]
    goods_weight = [3,4,5]
    
    def optimalDecision(decisions,status,profit,optimal_profit_next,weight):
        optimal_decision = None
        optimal_profit = -1
        for i in decisions:
            if profit(i) + optimal_profit_next[status - i*weight][1] > optimal_profit:
                optimal_profit = profit(i) + optimal_profit_next[status - i*weight][1]
                optimal_decision = i
        return optimal_decision,optimal_profit
    
    x = [{},{},{},{}]   # 状态 -> (最优决策,最优收益)
    for status in range(11):
        x[3][status] = (0,0)

    for i in range(3)[::-1]:
        for status in range(11):
            decisions = []
            for decision in range(5):
                if status - decision * goods_weight[i] >= 0:
                    decisions.append(decision)
            x[i][status] = optimalDecision(decisions,status,profitList[i],x[i+1],goods_weight[i])
    
    for step in x:print(step)
            
    optimal_decisions = [-1] * 3
    weight_left = 10
    for step in range(len(optimal_decisions)):
        optimal_decisions[step] = x[step][weight_left][0]
        weight_left = weight_left - optimal_decisions[step] * goods_weight[step]
    print(optimal_decisions)
    
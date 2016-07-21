if __name__ == '__main__':
    # x1 + x2 + x3 = 10    
    def profit1(a):return 4*a
    def profit2(a):return 9*a
    def profit3(a):return 2*a*a
    def profit4(a):return 0
    profitList = [profit1,profit2,profit3,profit4]
    
    def optimalDecision(decisions,status,profit,optimal_profit_next):
        optimal_decision = None
        optimal_profit = -1
        for i in decisions:
            if profit(i) + optimal_profit_next[status - i][1] > optimal_profit:
                optimal_profit = profit(i) + optimal_profit_next[status - i][1]
                optimal_decision = i
        return optimal_decision,optimal_profit
    
    x = [{},{},{},{}]   # 
    for status in range(11):
        x[3][status] = (0,0)

    for i in range(3)[::-1]:
        for status in range(11):
            decisions = []
            for decision in range(status+1):
                decisions.append(decision)
            x[i][status] = optimalDecision(decisions,status,profitList[i],x[i+1])
    
    for step in x:print(step)
            
    optimal_decisions = [-1] * 3
    resource = 10
    for step in range(len(optimal_decisions)):
        optimal_decisions[step] = x[step][resource][0]
        resource = resource - optimal_decisions[step]
    print(optimal_decisions)
    
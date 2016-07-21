# -*- coding=utf-8 -*-
if __name__ == '__main__':
    distance = [[0,6,7,9],[8,0,9,7],[5,8,0,8],[6,5,5,0]]
    
    #状态定义为现在所在地点，需要经过的地点集合。终点均为地点1
    #决策定义为下一步要去的地点
    
    city_set1 = [(1,'2:3:4')]
    city_set2 = [(2,'3:4'),(3,'2:4'),(4,'2:3')]
    city_set3 = [(3,'2'),(3,'4'),(2,'3'),(2,'4'),(4,'2'),(4,'3')]
    city_set4 = [(2,''),(3,''),(4,'')]
    status_set = [city_set1,city_set2,city_set3,city_set4]
    
    def optimalDecision(status,distance,optimal_distance_next):
        optimal_distance = float('inf')
        optimal_decision = None
        for decision in status[1].split(':'):
            city_set_next = status[1].split(':')
            city_set_next.remove(decision)
            city_set_next = ':'.join(city_set_next)
            decision = int(decision)
            distance_now = distance[status[0]-1][decision-1] + optimal_distance_next[(decision,city_set_next)][1]
            if distance_now < optimal_distance:
                optimal_distance = distance_now
                optimal_decision = decision
        return optimal_decision,optimal_distance
    
        
    x = [{},{},{},{}]
    for city in range(2,5):
        x[-1][(city,'')] = (1,distance[city-1][0])
    
    decisions = [-1] * 3    
    for step in range(3)[::-1]:
        for status in status_set[step]:
            x[step][status] = optimalDecision(status,distance,x[step+1])
    
    
    
    for i in x:print(i)
    
    decisions = [1] * 4
    status = '2:3:4'
    for step in range(1,4):
        decisions[step] = x[step-1][(decisions[step-1],status)][0]
        status = status.split(':')
        status.remove(str(decisions[step]))
        status = ':'.join(status)
        print(status)
    print(decisions)
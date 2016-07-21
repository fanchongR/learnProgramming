
if __name__ == '__main__':
    def optimalBuy(a):
        optimalBuyHelper(a,0,len(a)-1)
    def optimalBuyHelper(a,start,end):
        if start == end:
            return 0,0
        cutoff = int((start+end)/2)
        leftBuyDay,leftSellDay,leftProfit = optimalBuyHelper(a,start,cutoff)
        rightBuyDay,rightSellDay,rightProfit = optimalBuyHelper(a,cutoff+1,end)
        
        leftMinDay = start
        leftMinPrice = a[start]
        point = start
        while point <= cutoff:
            if a[point] < leftMinPrice:
                leftMinDay = point
                 
        rightMaxDay = end
        
        middleProfit = a[cutN+rightMaxDay] - a[leftMinDay]
        if middleProfit > leftProfit and middleProfit > rightProfit:
            return leftMinDay,cutN+rightMaxDay,middleProfit
        elif leftProfit > rightProfit:
            return leftMinDay,leftMaxDay,leftProfit
        else:
            return cutN+rightMinDay,cutN+rightMaxDay,rightProfit
        
        
    print(optimalBuy([3,5,1,2,7,9,1]))
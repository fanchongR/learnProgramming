# -*- coding=utf-8 -*-

#result is wrong, but leave it alone...
if __name__ == '__main__':
    def recursiveMiltiply(x,y): #x y位数相同
        N = len(str(x))
        if N == 1:
            return x*y
        
        leftN = N//2
        x1 = x // (10**leftN)
        x2 = x % (10**leftN)
        y1 = y // (10**leftN)
        y2 = y % (10**leftN)
        #print(x1,x2,y1,y2)
        p = recursiveMiltiply(x1+x2,y1+y2)
        a = recursiveMiltiply(x1,y1)
        b = recursiveMiltiply(x2,y2)
        print(x,y,p,a,b)
        return a*(10**N) + (p - a - b) * (10**leftN) + b
        
        
    print(recursiveMiltiply(123,324))
if __name__ == '__main__':
    def findPeak(a):
        N = len(a)
        if N < 2:
            return a
        elif N == 2:
            if a[0] > a[1]:return a[0]
            else:return a[1]
        
        cutN = N//2
        if a[cutN - 1] < a[cutN] and a[cutN] < a[cutN + 1]:
            return findPeak(a[cutN:])
        elif a[cutN - 1] > a[cutN] and a[cutN] > a[cutN + 1]:
            return findPeak(a[:(cutN+1)])
        else:
            return a[cutN]
        
    print(findPeak([2,3,4,6,8,6,3,1])) 
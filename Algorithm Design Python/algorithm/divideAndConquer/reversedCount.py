
if __name__ == '__main__':
    def mergeAndCount(a,b):
        i = 0
        j = 0
        count = 0
        c = []
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                c.append(b[j])
                j += 1
                count += len(a) - i
            else:
                c.append(a[i])
                i += 1
                
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return count,c
            
    def sortAndCount(a):
        if len(a) == 1:
            return 0,a
        
        n = int(len(a)/2)
        countLeft,aLeft = sortAndCount(a[:n])
        countRight,aRight = sortAndCount(a[n:])
        count,c = mergeAndCount(aLeft,aRight)
        count = count + countLeft + countRight
        return count,c
    
    print(sortAndCount([2,4,1,3,5]))
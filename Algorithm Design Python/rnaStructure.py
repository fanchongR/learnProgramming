if __name__ == '__main__':
    #a = 'ACCGGUAGU'
    a = 'ACAUGAUGGCCAUGU'
    N = len(a)
    
    def is_match(base1,base2):
        if set(base1+base2) == set('CG') or set(base1+base2) == set('AU'):
            return True
        else:
            return False
        
    OPT = [[0 for i in range(N)] for j in range(N)]
    CONNECT = [[-1 for i in range(N)] for j in range(N)]
    STRUCTURE = [0 for i in range(N)]
    for k in range(5,N):
        for i in range(N-k):
            j = i + k
            OPTnot = OPT[i][j-1]
            optimalConnect = -1
            optimalOPTConnect = OPTnot
            for t in range(i,j-4):
                if is_match(a[j],a[t]):
                    if t == i and OPT[t+1][j-1] + 1 >= optimalOPTConnect:
                        optimalOPTConnect = OPT[t+1][j-1] + 1
                        optimalConnect = t
                    elif t > i and OPT[i][t-1] + OPT[t+1][j-1] + 1 >= optimalOPTConnect:
                        optimalOPTConnect = OPT[i][t-1] + OPT[t+1][j-1] + 1
                        optimalConnect = t
            OPT[i][j] = optimalOPTConnect
            CONNECT[i][j] = optimalConnect
                        
    for i in OPT:
        print(i)
    for i in CONNECT:
        print(i)
    def rnaStructure(CONNECT,i,j):
        if i >= j - 4:
            return 
        if CONNECT[i][j] != -1:
            print("%d-%d" % (CONNECT[i][j],j))
            rnaStructure(CONNECT,i,CONNECT[i][j]-1)
            rnaStructure(CONNECT,CONNECT[i][j]+1,j-1)
    
    rnaStructure(CONNECT, 0, N-1)
    
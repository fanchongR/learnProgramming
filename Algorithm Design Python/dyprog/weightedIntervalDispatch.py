if __name__ == '__main__':
    weight = [0,2,4,4,7,2,1]
    p = [0,0,0,1,0,3,3]
    
    M = [0] * 7
    for i in range(1,7):
        if M[i-1] > weight[i] + M[p[i]]:
            M[i] = M[i-1]
        else:
            M[i] = weight[i] + M[p[i]]
    
    decisions = [0] * 7
    i = 6
    while i > 0:
        if M[i-1] > weight[i] + M[p[i]]:
            i -= 1
        else:
            decisions[i] = 1
            i = p[i]
    
    
    print(M)
    print(decisions)
    
    
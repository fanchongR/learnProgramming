
if __name__ == '__main__':
    graph = [-1,[4,5,7],[3,5,6],[4,5],[5],[6,7],[7],[]]
    vertex = 7
    in_degree = [0] * 8
    
    for v in range(1,vertex+1):
        for edge in graph[v]:
            in_degree[edge] += 1

    S = set()
    for v in range(1,vertex+1):
        if in_degree[v] == 0:
            S.add(v)
    
    result = []
    while len(S) > 0:
        v = S.pop()
        result.append(v)
        for edge in graph[v]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                S.add(edge)
                
    print(result)
    
    
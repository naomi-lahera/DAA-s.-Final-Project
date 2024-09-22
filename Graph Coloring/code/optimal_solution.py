from collections import deque
from typing import Tuple

maxn = 5000 + 5
color = [-1] * maxn
vertices = [[] for _ in range(2)]

def is_bipartite(u: int, edges) -> Tuple[int, int]:
    global color, vertices
    
    color[u] = 0
    Q = deque()
    Q.append(u)
    cnt = [0, 0]

    while len(Q) != 0:
        u = Q.popleft()
        cnt[color[u]] += 1
        vertices[color[u]][-1].append(u)

        for v in edges[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                Q.append(v)
            elif color[v] == color[u]:
                return (-1, -1)

    return (cnt[0], cnt[1])

def coloring_dp(n, n1, n2, n3, edges):
    global maxn, color, vertices
    
    color = [-1] * maxn
    vertices = [[], []]

    for i in range(1, n + 1):
        if color[i] == -1:
            vertices[0].append([])
            vertices[1].append([])
            
            (cnt1, cnt2) = is_bipartite(i, edges)
            if cnt1 == -1:
                # print('El grafo no es bipartito')
                return 'NO', None
     
        
    #? maxn es mayor que la cantidad de vertices que puede tener el grafo entonces siempre va a ser posible preguntar por dp[i][n]    
    dp = [[-1] * maxn for _ in range(maxn)]
    dp[0][0] = 0

    total_cc = len(vertices[0])
    for i in range(total_cc):
        for j in range(maxn):
            if dp[i][j] != -1:
                dp[i + 1][j + len(vertices[0][i])] = 0
                dp[i + 1][j + len(vertices[1][i])] = 1

    if dp[total_cc][n2] == -1:
        # print(f'No se pueden colocar {n2} nodos con el número 2')
        return 'NO', None

    ans = [-1] * (n + 1)
    for i in range(total_cc + 1, 0, 1):
        for u in vertices[dp[i][n2]][i - 1]:
            ans[u] = 2
        n2 -= len(vertices[dp[i][n2]][i])
    
    for i in range(1, n + 1):
        if ans[i] == -1:
            if n1 != 0:
                ans[i] = 1
                n1 -= 1
            else:
                ans[i] = 3
                n3 -= 1

    # print(ans)
    return 'YES', ''.join(map(str, ans[:1])) 

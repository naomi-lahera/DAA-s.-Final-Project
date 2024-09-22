from itertools import permutations

def check_valid(graph, labels):
    for u in range(len(graph)):
        for j in range(len(graph[u])):
            v = graph[u][j]
            if abs(labels[u-1] - labels[v-1]) != 1:
                return False
    return True


def brute_force(n, m, n1, n2, n3, edges):
    graph = edges
    
    labels = [1] * n1 + [2] * n2 + [3] * n3
    
    for perm in permutations(labels):
        if check_valid(graph, perm):
            return 'YES', ''.join(map(str, perm))
    
    return "NO", None
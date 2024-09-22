score = 0
def get_max(a, k, m):
    global score
    if k == 0 or m == len(a):
        score = max(get_score(a), score)
        return 
    
    for i in range(m, len(a)):
        if a[i][1] == 1:
            for j in range(k + 1):
                a[i] = (a[i][0] + j, 1)
                get_max(a, k - j,  i + 1)
                a[i] = (a[i][0] - j, 1)
                
def get_score(arr):
    arr = sorted(arr, key=lambda x: x[0])
    index = len(arr) // 2 - 1
    if index >= 0:
        return arr[-1][0] + arr[index][0]
    
def maximize_score_bf(a, k):
    global score
    score = get_score(a)
    get_max(a, k, 0)
    return score

def maximize_score_bs(a, k):
        a.sort()
        
        ans = 0
        # Incrementar el máximo
        for i in range(len(a)):
            if a[i][1] == 1:
                if i < len(a) // 2:
                    mc = a[len(a) // 2][0]
                else:
                    mc = a[(len(a) - 2) // 2][0]
                
                ans = max(ans, a[i][0] + k + mc)
        
        # Incrementar la mediana
        lo, hi = 0, int(2e9)
        while lo != hi:
            mid = (lo + hi + 1) // 2
            
            z = 0
            smaller_list = []
            for i in range(len(a) - 1):
                if a[i][0] >= mid:
                    z += 1
                elif a[i][1] == 1:
                    smaller_list.append(mid - a[i][0])  # Lista de números menores que mid pero con indicador 1
            
            print(smaller_list)
            smaller_list.sort(reverse=True) 
            
            kk = k
            for x in smaller_list:
                if kk >= x:
                    kk -= x
                    z += 1
            
            if z >= (len(a) + 1) // 2:
                lo = mid
            else:
                hi = mid - 1
        
        ans = max(ans, a[-1][0] + lo)
        
        return ans


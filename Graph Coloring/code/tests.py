import unittest
from brute_force import *
from optimal_solution import coloring_dp

class TestGraphColoring(unittest.TestCase):
    def test_brute_force(self):
        with open('test_cases.txt', 'r') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break 
                
                n, m = map(int, line.split())
                n1, n2, n3 = map(int, file.readline().split())
                
                edges = [[] for _ in range(n + 1)]
                for _ in range(m):
                    a, b = map(int, file.readline().split())
                    edges[a].append(b)
                    edges[b].append(a)
                
                exist = file.readline().strip()
                file.readline().strip()
    
                bf, bf_sol = brute_force(n, m, n1, n2, n3, edges)
                
                self.assertEqual(exist, bf)
                
                if exist == 'YES':
                    # print(bf_sol)
                    for i in range(n):
                        for j in range(i+1, len(edges[i])):
                            v = edges[j][i]
                            self.assertEqual(abs(bf_sol[i] - bf_sol[v-1]), 1)
                            
    def test_optimal_solution(self):
        with open('test_cases.txt', 'r') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break 
                
                n, m = map(int, line.split())
                
                n1, n2, n3 = map(int, file.readline().split())
                
                edges = [[] for _ in range(n + 1)]
                for _ in range(m):
                    a, b = map(int, file.readline().split())
                    edges[a].append(b)
                    edges[b].append(a)
                
                exist = file.readline().strip()
                file.readline().strip()
    
                bf, bf_sol = coloring_dp(n, n1, n2, n3, edges)
                
                self.assertEqual(exist, bf)
                
                if exist == 'YES':
                    # print(bf_sol)
                    for i in range(n):
                        for j in range(i+1, len(edges[i])):
                            v = edges[j][i]
                            self.assertEqual(abs(bf_sol[i] - bf_sol[v-1]), 1)
                        

if __name__ == '__main__':
    unittest.main()

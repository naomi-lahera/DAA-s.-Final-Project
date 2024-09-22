import unittest
from brute_force import maximize_score_bf
from optimal_solution import maximize_score_bs

class TestGraphColoring(unittest.TestCase):
    def test_binary_search(self):
        t = 0
        test_cases = []
        
        with open('test_cases.txt', 'r') as file:
            line = file.readline().strip()
            if not line: return 
            t = int(line)
            
            for _ in range(t):
                line = file.readline().strip()
                if not line:
                    break 
                
                n, k = map(int, line.split())
                
                first_list = list(map(int, file.readline().split()))
                second_list = list(map(int, file.readline().split()))
                a = list(zip(first_list, second_list))
                test_cases.append((a, k))
                
            file.readline()
            
            expected_output = []
            for _ in range(t):
                expected_output.append(int(file.readline()))
        
        for i in range(len(test_cases)):
            print('k: ', test_cases[i][1])
            print('Array: ', test_cases[i][0])
            print('Expected: ', expected_output[i])
            score = maximize_score_bs(test_cases[i][0], test_cases[i][1])
            self.assertEqual(score, expected_output[i])
            print('Score: ', score)
            print()
            
    def test_brute_force(self):
        t = 0
        test_cases = []
        
        with open('test_cases.txt', 'r') as file:
            line = file.readline().strip()
            if not line: return 
            t = int(line)
            
            for _ in range(t):
                line = file.readline().strip()
                if not line:
                    break 
                
                n, k = map(int, line.split())
                
                first_list = list(map(int, file.readline().split()))
                second_list = list(map(int, file.readline().split()))
                a = list(zip(first_list, second_list))
                test_cases.append((a, k))
                
            file.readline()
            
            expected_output = []
            for _ in range(t):
                expected_output.append(int(file.readline()))
        
        for i in range(len(test_cases)):
            print('k: ', test_cases[i][1])
            print('Array: ', test_cases[i][0])
            print('Expected: ', expected_output[i])
            score = maximize_score_bf(test_cases[i][0], test_cases[i][1])
            self.assertEqual(score, expected_output[i])
            print('Score: ', score)
            print()

if __name__ == '__main__':
    unittest.main()


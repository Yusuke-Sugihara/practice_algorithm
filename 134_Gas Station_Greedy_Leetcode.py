import time
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
    
    
# test case1
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]

# test case2
gas = [2, 3, 4]
cost = [3, 4, 3]

solution = Solution()
start_time = time.time()
result = solution.canCompleteCircuit(gas, cost)
end_time = time.time()

execution_time = round(end_time - start_time,8)
# print result and time
print(f'result: {result}')
print(f'execution time : {execution_time} sec')
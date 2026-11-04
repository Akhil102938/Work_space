from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, completing the circuit is impossible
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        # Check each station once
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # If the tank becomes negative, this start cannot work
            if tank < 0:
                start = i + 1
                tank = 0

        return start
      

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            
            # Can't reach station i+1 from current start
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total_gas >= total_cost else -1
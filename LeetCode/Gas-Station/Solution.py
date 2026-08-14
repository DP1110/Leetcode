1class Solution(object):
2    def canCompleteCircuit(self, gas, cost):
3        total_gas = 0
4        total_cost = 0
5        tank = 0
6        start = 0
7        
8        for i in range(len(gas)):
9            total_gas += gas[i]
10            total_cost += cost[i]
11            tank += gas[i] - cost[i]
12            
13            # Can't reach station i+1 from current start
14            if tank < 0:
15                start = i + 1
16                tank = 0
17        
18        return start if total_gas >= total_cost else -1
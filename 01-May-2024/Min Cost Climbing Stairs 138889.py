# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3,-1,-1):
            cost[i]  = min(cost[i] + cost[i+1] , cost[i] + cost[i+2])
        
        print(cost)
        return cost[0] if cost[0] < cost[1] else cost[1]
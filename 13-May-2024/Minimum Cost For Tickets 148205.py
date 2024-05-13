# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dp(i):
            if i == len(days):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = float('inf')
            for day, cost in zip([1, 7, 30], costs):
                dist = i
                while dist < len(days) and days[dist] < days[i] + day:
                    dist += 1
                memo[i] = min(dp(i), cost + dp(dist))

            return memo[i]

        return dp(0)
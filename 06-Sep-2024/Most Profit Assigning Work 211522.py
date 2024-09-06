# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        # print(jobs)
        mx = []
        mx_profit = 0
        
        for d, p in jobs:
            mx_profit = max(mx_profit, p)
            mx.append((d, mx_profit))
        
        def calc(num):
            left, right = 0, len(mx) - 1
            while left <= right:
                mid = (left + right) // 2
                if mx[mid][0] <= num:
                    left = mid + 1
                else:
                    right = mid - 1
            return mx[right][1] if right >= 0 else 0
        
        res = 0
        for num in worker:
            res += calc(num)
        # print(mx)
        return res

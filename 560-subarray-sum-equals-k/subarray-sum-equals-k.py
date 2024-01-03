class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        current = 0
        prefix_sum = {0:1}

        for n in nums:
            current += n
            ans += prefix_sum.get(current-k, 0)
            prefix_sum[current] = 1 + prefix_sum.get(current, 0)

        return ans

            



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        current = 0
        res = 0

        for i in range(len(nums)):
            current += nums[i]
            if current - k in prefix:
                res += prefix[current - k]  
            prefix[current] += 1 
        return res

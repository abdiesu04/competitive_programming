class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix  = defaultdict(int)
        prefix[0] = 1
        res  = 0

        current  = 0
        for i in range(len(nums)):
            current += nums[i]
            remainder = current % k
            res += prefix[remainder]
            prefix[remainder] += 1

        return res

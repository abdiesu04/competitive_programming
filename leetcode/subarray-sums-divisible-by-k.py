class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        count = [0] * k
        for sum in prefix_sums:
            count[sum % k] += 1
        
        ans = 0
        for c in count:
            ans += c * (c-1) // 2
        
        return ans
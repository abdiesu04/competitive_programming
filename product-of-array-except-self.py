class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, answer = [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] = prefix[i] * suffix
            suffix *= nums[i]
        
        return answer

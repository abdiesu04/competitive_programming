class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre , suff = 1 , 1
        ans = float('-inf')
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1

            pre *= nums[i]
            suff *= nums[len(nums) - i  - 1] 
            
            ans = max(ans , max(pre , suff))

        return ans
            
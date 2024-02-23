# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         length=len(nums)
#         sol=[1]*length
#         pre = 1
#         post = 1
#         for i in range(length):
#             sol[i] *= pre
#             pre = pre*nums[i]
#             sol[length-i-1] *= post
#             post = post*nums[length-i-1]
#         return(sol)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1] * len(nums)
        pre = [1] * len(nums)
        
        s = 1
        for i in range(len(nums)):
            s *= nums[i]
            pre[i] = s
        
        s = 1
        for i in range(len(nums) - 1, -1, -1):
            s *= nums[i]
            post[i] = s
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(post[i + 1])
            elif i == len(nums) - 1:
                res.append(pre[i - 1])
            else:
                res.append(pre[i - 1] * post[i + 1])
        
        return res

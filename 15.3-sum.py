#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
            # Brute Force
            # nums.sort()
            # res = []
            # for i in range(len(nums)):
            #     for j in range(i+1, len(nums)):
            #         for k in range(j+1, len(nums)):
            #             if nums[i] + nums[j] + nums[k] == 0:
            #                 if [nums[i], nums[j], nums[k]] not in res:
            #                     res.append([nums[i], nums[j], nums[k]])
            # return res
            
            # Two Pointers
            nums.sort()
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    l, r = i+1, len(nums)-1
                    while l < r:
                        s = nums[i] + nums[l] + nums[r]
                        if s < 0:
                            l += 1
                        elif s > 0:
                            r -= 1
                        else:
                            res.append([nums[i], nums[l], nums[r]])
                            while l < r and nums[l] == nums[l+1]: 
                                l += 1
                            while l < r and nums[r] == nums[r-1]: 
                                r -= 1
                            l += 1
                            r -= 1
            return res
            
            # Two Pointers (Optimized)
            # nums.sort()
            # res = []
            # for i in range(len(nums)):
            #     if i == 0 or nums[i] != nums[i-1]:
            #         l, r = i+1, len(nums)-1
            #         while l < r:
            #             s = nums[i] + nums[l] + nums[r]
            #             if s < 0:
            #                 l += 1
            #             elif s > 0:
            #                 r -= 1
            #             else:
            #                 res.append([nums[i], nums[l], nums[r]])
            #                 while l < r and nums[l] == nums[l+1]: 
            #                     l += 1
            #                 while l < r and nums[r] == nums[r-1]: 
            #                     r -= 1
            #                 l += 1
            #                 r -= 1
            # return res
            
            #
        
# @lc code=end


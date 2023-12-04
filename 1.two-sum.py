#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            
            # Brute Force
            # for i in range(len(nums)):
            #     for j in range(i+1, len(nums)):
            #         if nums[i] + nums[j] == target:
            #             return [i, j]
    
            # Hash Table
            # hash_table = {}
            # for i in range(len(nums)):
            #     if nums[i] in hash_table:
            #         return [hash_table[nums[i]], i]
            #     else:
            #         hash_table[target - nums[i]] = i
    
            # Hash Table (One-pass)
            hash_table = {}
            for i in range(len(nums)):
                if nums[i] in hash_table:
                    return [hash_table[nums[i]], i]
                else:
                    hash_table[target - nums[i]] = i
    
            return [-1, -1]
        
# @lc code=end


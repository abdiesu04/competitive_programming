# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         #Generic k-sum
    
#         #Manual 3sum
#         nums.sort()

#         triplets = []
#         triplet_set = set()

#         for i in range(len(nums)-2):
#             j = i+1
#             k = len(nums) - 1

#             while j < k:
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     if tuple([nums[i], nums[j], nums[k]]) not in triplet_set:
#                         triplet_set.add(tuple([nums[i], nums[j], nums[k]]))
#                         triplets.append([nums[i], nums[j], nums[k]])
#                     j += 1
                
#                 elif nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 else:
#                     k -= 1
        
#         return triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

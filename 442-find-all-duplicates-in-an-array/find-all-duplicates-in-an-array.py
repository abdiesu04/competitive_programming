# solved using constant extra space

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         res = []
#         for n in nums:
#             i = abs(n) -  1
#             if nums[i] > 0:
#                 nums[i] = -1 * nums[i]
#             else:
#                 res.append(i + 1)
#         return res
        

#using set

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set([])
        cur = set()
        for num in nums:
            if num in cur: res.add(num)
            else: cur.add(num)
        return res    
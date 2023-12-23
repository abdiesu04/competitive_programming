# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort()
#         mx = 0
#         for i in range(len(nums)-1,1, -1):
#             if nums[i-2] + nums[i-1] > nums[i]:
#                 mx = max(mx , nums[i-2] + nums[i-1] + nums[i] )
#         return mx

class Solution(object):
    def largestPerimeter(self, A):
        A.sort(reverse=True)

        for i in range(len(A)-2):
            a = A[i]
            b= A[i+1]
            c = A[i+2]
            if a< b+ c:
                return a+b+c
            
        return 0

        
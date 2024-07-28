class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        def check(a , b, c):
            return (
                a + b > c and
                a + c > b and
                b + c > a
            )

        for i in range(len(nums) - 2):
            if check(nums[i] , nums[i+1] , nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

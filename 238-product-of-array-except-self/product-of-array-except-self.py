class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * (len(nums) + 1)
        accumulator  = 1
        for i in range(len(nums)):
            accumulator  *= nums[i]
            prefix.append(accumulator)
        accumulator  = 1
        for i in range(len(nums)-1 , -1 , -1):
            accumulator  *= nums[i]
            postfix[i] = accumulator
        print(prefix)
        print(postfix)
        result = []
        for i in range(len(prefix) -1):
            result.append(prefix[i] * postfix[i+1])

        return result
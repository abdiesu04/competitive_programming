class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def isEven(n):
            return n % 2 == 0
        prefix = [1]
        cnt = 1
        for i in range(1 , len(nums)):
            if isEven(nums[i]) == isEven(nums[i-1]):
                cnt = 0
                prefix.append(0)
            else:
                cnt += 1
                prefix.append(cnt)
       
        result  = []
        for start , end in queries:
            if prefix[start] - prefix[end] + 1 == start - end + 1:
                result.append(True)
            else:
                result.append(False)
        return result




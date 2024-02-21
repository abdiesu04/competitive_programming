class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        evenSum  = 0
        for i in nums:
            if i % 2 == 0:
                evenSum += i
        
        for add , idx in queries:
            tmp = add + nums[idx]
            if tmp % 2 == 0 and nums[idx] % 2 != 0:
                evenSum += tmp
                res.append(evenSum)
            elif tmp % 2 != 0 and nums[idx] % 2 == 0:
                evenSum -= nums[idx]
                res.append(evenSum)
            elif tmp % 2 == 0 and nums[idx] % 2 == 0:
                evenSum += add
                res.append(evenSum)
            else:
                res.append(evenSum)
            nums[idx] = tmp
        return res

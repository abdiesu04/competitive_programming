class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        distances = defaultdict(list)
        for index, num in enumerate(nums):
            distances[num].append(index) 
        output = [0] * len(nums)
        for values in distances.values():
            n = len(values)
            if n > 1:
                rSum = sum(values)
                lSum = 0
                prevVal = 0
                for i, val in enumerate(values):
                    dist = val - prevVal
                    rSum -= (n-i) * dist
                    lSum += dist * i
                    prevVal = val
                    output[val] = rSum + lSum
        return output
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        for i in hash.values():
            if i > 1:
                return True
        return False

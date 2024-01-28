
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        cnt = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] == target:
                cnt[target].append(i)
        return [cnt[target][0], cnt[target][-1]] if cnt[target] else [-1,-1]
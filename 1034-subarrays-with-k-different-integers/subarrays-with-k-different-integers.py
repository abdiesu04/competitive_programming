class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        mapp = defaultdict(int)
        ans = 0
        count = 0

        while r < len(nums):
            mapp[nums[r]] += 1

            while len(mapp) > k:
                mapp[nums[l]] -= 1
                if mapp[nums[l]] == 0:
                    del mapp[nums[l]]
                l += 1
                count = 0

            while mapp[nums[l]] > 1:
                mapp[nums[l]] -= 1
                l += 1
                count += 1

            if len(mapp) == k:
                ans += count + 1

            r += 1

        return ans
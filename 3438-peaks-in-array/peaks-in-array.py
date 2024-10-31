class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (2 * self.n)
        self.build()

    def build(self):
        for idx in range(self.n):
            self.tree[idx + self.n] = self.arr[idx]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        self.arr[index] = value
        index += self.n
        self.tree[index] = value

        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, l, r):
        l += self.n
        r += self.n
        result = 0

        while l < r:
            if l % 2 == 1:
                result += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                result += self.tree[r]
            l //= 2
            r //= 2
        return result

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        peaks = [0] * len(nums)
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                peaks[i] = 1

        tree = SegmentTree(peaks)
        res = []

        for op, one, two in queries:
            if op == 1:
                res.append(tree.query(one+1, two))
                # print(one , two , peaks)
            else:
                nums[one] = two
                if one > 0 and one < len(nums) - 1:
                    peaks[one] = int(nums[one - 1] < nums[one] > nums[one + 1])
                if one > 1:
                    peaks[one - 1] = int(nums[one - 2] < nums[one - 1] > nums[one])
                if one < len(nums) - 2:
                    peaks[one + 1] = int(nums[one] < nums[one + 1] > nums[one + 2])

                tree.update(one, peaks[one])
                if one > 1:
                    tree.update(one - 1, peaks[one - 1])
                if one < len(nums) - 2:
                    tree.update(one + 1, peaks[one + 1])

        return res

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        left = k % sm
        for i in range(len(chalk)):
            if left - chalk[i] < 0:
                return i
            left -= chalk[i]

# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = defaultdict(int)
        # print(dp)
        answer = 1
        for a in arr:
            # print(a,a-diff)
            before_a = dp[a - diff]
            dp[a] = before_a + 1
            # print(a,before_a + 1)
            answer = max(answer, dp[a])
            
        return answer
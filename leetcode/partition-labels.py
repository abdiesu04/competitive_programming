class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = defaultdict(int)
        for i , c in enumerate(s):
            lastOccurence[c] = i

        ans , left , right = [] , -1, -1
        for i , c in enumerate(s):
            right  = max(right ,lastOccurence[c] )
            if i == right:
                ans.append(right - left)
                left = i
        return ans


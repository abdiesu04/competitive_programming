class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs , key = len)
        print(strs)
        arr = zip(*strs)
        res = 0
        for i  in arr:
            if len(set(i)) == 1:
                res += 1
            else:
                break
        return strs[0][:res]

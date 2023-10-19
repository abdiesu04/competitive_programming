class Solution:
    def repeatedCharacter(self, s: str) -> str:
        arr = []
        for i in s:
            if i not in arr:
                arr.append(i)
            else:
                return i
                break
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left, right = 0, 0

        while left < len(str1) and right < len(str2):
            if str1[left] == str2[right]:
                left += 1
                right += 1
            else:
                if (ord(str1[left]) + 1 - ord('a')) % 26 + ord('a') == ord(str2[right]):
                    left += 1
                    right += 1
                else:
                    left += 1

        return right == len(str2)

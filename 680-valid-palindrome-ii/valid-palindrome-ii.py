class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0 , len(s)-1
        while left < right:
            if s[left] != s[right]:
                if self.isPalindrome(s , left + 1, right):
                    return True
                elif self.isPalindrome(s, left, right-1):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True


    def isPalindrome(self, s:str, left:int , right:int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

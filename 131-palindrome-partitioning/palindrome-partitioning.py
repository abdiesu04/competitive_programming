class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        res = []

        def backtrack(index , path):
            if index == len(s):
                res.append(path[:])
                return 

            for i in range(index , len(s)):
                current  = s[index:i+1]
                if isPalindrome(current):
                    path.append(current)
                    backtrack(1 + i ,path )
                    path.pop()

        backtrack(0 , [])
        return res
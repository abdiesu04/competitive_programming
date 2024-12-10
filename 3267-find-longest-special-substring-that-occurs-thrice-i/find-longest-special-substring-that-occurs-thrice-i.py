class Solution:
    def maximumLength(self, s: str) -> int:
        mapp = defaultdict(int)
        left = 0

        def changeToMapp(substring:str):
            letter  = substring[0]
            print(substring , letter)
            n = len(substring)
            for i in range(1,n+1):
                mapp[(letter*n , n)] += i
                n -= 1

        for right in range(1,len(s)):
            if s[right] != s[left]:
                changeToMapp(s[left:right])
                left = right
        changeToMapp(s[left:len(s)])

        print(mapp)
            
        ans = -1
        for key , val in mapp.items():
            if val > 2:
                ans  = max(ans , key[1])
        return ans
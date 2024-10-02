class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        s_count = defaultdict(int)
        t_set = set(t)

        need = len(required)
        have = 0
        ans  = ""

        left  = 0 
        res  = float('inf')

        for right in range(len(s)):
            if s[right] in t_set:
                s_count[s[right]] += 1
                if  s_count[s[right]] == required[s[right]]:
                    have += 1
            # print(s_count , have , need , res)
            while have == need:
                if res >  right - left + 1:
                    res  =  right - left + 1
                    ans  = s[left:right+1]

                res = min(res , right - left + 1)
                if s[left] in t_set:
                    s_count[s[left]] -= 1
                    if s_count[s[left]] < required[s[left]]:
                        have -= 1
                left += 1
        

        return ans 



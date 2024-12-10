class Solution:
    def maximumLength(self, s: str) -> int:
        left, right = 0, len(s)

        def canI(length):

            mapp = defaultdict(int)  
            for i in range(len(s) - length + 1):
                subs = s[i:i + length] 
                if len(set(subs)) == 1: 
                    mapp[subs] += 1  
                    if mapp[subs] >= 3: 
                        return True 
            return False 

        while left < right:
            mid = left + (right - left + 1) // 2  
            if canI(mid):
                left = mid  
            else:
                right = mid - 1  

        return right if right > 0 and canI(right) else -1

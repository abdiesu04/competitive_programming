class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        mapp = defaultdict(int)
        cnt = 0 

        for i in ans:
            if i == 0:
                cnt += 1
            elif i not in mapp or mapp[i] == 0:
                mapp[i] = 1
                cnt += i + 1
            else:
                mapp[i] += 1
                if mapp[i] > i:
                    mapp[i] = 0
        return cnt
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapp = [0, 0, 0]
        for i in bills:
            if i == 5:
                mapp[0] += 1
            elif i == 10:
                if mapp[0] == 0:
                    return False
                mapp[0] -= 1
                mapp[1] += 1
            else:
                if mapp[1] >= 1 and mapp[0] >= 1:
                    mapp[1] -= 1
                    mapp[0] -= 1
                elif mapp[0] >= 3:
                    mapp[0] -= 3
                else:
                    return False
        return True
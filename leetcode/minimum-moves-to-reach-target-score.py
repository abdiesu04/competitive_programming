class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0: return target - 1
        cnt = 0
        while target != 1:
            if target % 2:
                target -= 1
                cnt += 1
            else:
                if maxDoubles == 0:
                    break
                else:
                    target = target // 2
                    maxDoubles -= 1
                    cnt += 1
        cnt += target - 1
        return cnt
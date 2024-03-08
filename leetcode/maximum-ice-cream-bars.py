class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        temp = 0
        cnt = 0
        for i in costs:
            temp += i
            if temp <= coins:
                cnt += 1
            else:
                break
        return cnt

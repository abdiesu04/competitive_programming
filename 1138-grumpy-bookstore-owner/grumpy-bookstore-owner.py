from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        alls = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                alls += customers[i]

        add = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                add += customers[i]

        max_add = add

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                add += customers[i]
            if grumpy[i - minutes] == 1:
                add -= customers[i - minutes]

            max_add = max(max_add, add)

        return alls + max_add

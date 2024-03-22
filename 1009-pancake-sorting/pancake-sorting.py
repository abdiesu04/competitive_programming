from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n - 1, 0, -1):
            mx = max(arr[:i + 1])
            mx_index = arr.index(mx)
            if mx_index != i:
                res.append(mx_index + 1)
                res.append(i + 1)
                arr[:mx_index + 1] = arr[:mx_index + 1][::-1]
                arr[:i + 1] = arr[:i + 1][::-1]
        return res
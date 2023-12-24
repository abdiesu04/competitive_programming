class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] == 2 * arr[i] or arr[j] * 2 == arr[i]:
                    return True
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return False
        n=len(matrix)
        m = len(matrix[0])
        low = 0
        high=n-1
        while low <= high:
            mid = (low+high)//2
            l = 0
            h = m-1
            while l<=h:
                mmid = (l+h)//2
                if matrix[mid][mmid] == target:
                    return True
                elif matrix[mid][mmid] > target:
                    h = mmid -1
                else:
                    l = mmid+1
            if matrix[mid][0] > target:
                high = mid -1
            else:
                low = mid +1
        return False
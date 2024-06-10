class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def returnMaxIdx(row):
            mx = -1
            idx = -1
            for i in range(len(mat[0])):
                if mat[row][i] > mx:
                    mx = mat[row][i]
                    idx = i
            return idx

        low = 0
        high = len(mat)

        while low < high:
            mid = low + (high - low) // 2
            max_idx = returnMaxIdx(mid)
            top = mat[mid-1][max_idx] if mid - 1 >= 0 else -1
            bottom = mat[mid+1][max_idx] if mid + 1 < len(mat) else -1
            current = mat[mid][max_idx]
            if current > top and current > bottom:
                return [mid, max_idx]
            elif current < top:
                high = mid
            else:
                low = mid + 1
        return [-1, -1]

        #time  - O(n(log(m)))
        #space - constant
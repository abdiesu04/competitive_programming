class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        total = maximumHeight[0]
        
        for i in range(1, len(maximumHeight)):
            if maximumHeight[i] >= maximumHeight[i-1]:
                maximumHeight[i] = maximumHeight[i-1] - 1
            
            if maximumHeight[i] <= 0:
                return -1
            
            total += maximumHeight[i]
        
        return total

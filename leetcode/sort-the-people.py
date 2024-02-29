class Solution:
    def selectionSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1,n):
                if arr[j] > arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    


    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = dict(zip(heights,names))
        self.selectionSort(heights)
        output = []
        for i in heights:
            output.append(heightDict[i])
        return output



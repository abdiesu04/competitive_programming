class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]


    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = dict(zip(heights,names))
        self.bubbleSort(heights)
        output = []
        for i in heights:
            output.append(heightDict[i])
        return output



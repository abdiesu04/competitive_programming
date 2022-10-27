class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        num=len(arr)
        output=[]
        while(num>0):
            i=arr.index(num)
            arr[0:i+1]=arr[0:i+1][::-1]
            output.append(i+1)
            arr[0:num]=arr[0:num][::-1]
            output.append(num)
            num-=1
        return output

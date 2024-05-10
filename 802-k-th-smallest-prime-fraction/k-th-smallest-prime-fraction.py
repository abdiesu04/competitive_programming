class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        heap = []
        
        for i in range(len(arr)):
           heappush(heap, ((arr[i] / arr[-1]), i, len(arr) - 1))
 
        for _ in range(k - 1):
            cur =heappop(heap)
            num_idx = cur[1]
            den_idx = cur[2] - 1
            if den_idx > num_idx:
               heappush(heap, (
                    (arr[num_idx] / arr[den_idx]), 
                    num_idx, 
                    den_idx
                ))

        
        res =heappop(heap)
        return [arr[res[1]], arr[res[2]]]
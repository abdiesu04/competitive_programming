class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_set = set(nums)
        count,i = 0 ,0
        hm = defaultdict(int) #hash map 

        for j in nums : 
            hm[j] += 1
            while len(unique_set) == len(hm):
                if hm[nums[i]] == 1 :
                    hm.pop(nums[i])
                else : 
                    hm[nums[i]] -= 1
                i += 1
            count += i
        return count


                
                
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Generic k-sum
    
        #Manual 3sum
        nums.sort()

        triplets = []
        triplet_set = set()

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if tuple([nums[i], nums[j], nums[k]]) not in triplet_set:
                        triplet_set.add(tuple([nums[i], nums[j], nums[k]]))
                        triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return triplets

        
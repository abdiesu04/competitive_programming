
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        
        sorted_nums = sorted(freq_map.items(), key=lambda x: (x[1], -x[0]))
        
        result = []
        for num, count in sorted_nums:
            result.extend([num] * count)
        
        return result
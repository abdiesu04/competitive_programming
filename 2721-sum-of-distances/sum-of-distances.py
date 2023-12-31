class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        count_dict = defaultdict(list)

        for i, num in enumerate(nums):
            count_dict[num].append(i)

        for key, values in count_dict.items():
            if len(values) == 1:
                res[values[0]] = 0
            else:
                suffix_sum = sum(values)
                prefix_sum = 0

                for i in range(len(values)):
                    cur_idx = count_dict[key][i]
                    cur_sum = (i * cur_idx - prefix_sum) + (suffix_sum - cur_idx - (len(values) - 1 - i) * cur_idx) 
                    res[cur_idx] = cur_sum
                    prefix_sum += cur_idx
                    suffix_sum -= cur_idx
        
        return res
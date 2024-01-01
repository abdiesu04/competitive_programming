class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sums = []
        for sublist in wall:
            prefix_sum = [0]
            for i in range(len(sublist)):
                prefix_sum.append(prefix_sum[-1] + sublist[i])
            prefix_sums.append(prefix_sum[1:-1])  # Exclude the first and last elements

        mapp = defaultdict(int)

        for prefix_sum in prefix_sums:
            for num in prefix_sum:
                mapp[num] += 1

        max_count = 0
        for count in mapp.values():
            max_count = max(max_count, count)

        return len(wall) - max_count
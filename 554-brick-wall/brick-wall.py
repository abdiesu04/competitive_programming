# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         prefix_sums = []
#         for sublist in wall:
#             prefix_sum = [0]
#             for i in range(len(sublist)):
#                 prefix_sum.append(prefix_sum[-1] + sublist[i])
#             prefix_sums.append(prefix_sum[1:-1])  # Exclude the first and last elements

#         mapp = defaultdict(int)

#         for prefix_sum in prefix_sums:
#             for num in prefix_sum:
#                 mapp[num] += 1

#         max_count = 0
#         for count in mapp.values():
#             max_count = max(max_count, count)

#         return len(wall) - max_count

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # You want the location the occurs the most as a left (or right) edge of a brick; in worst case, 
        # there are no edges in the middle so you need to cut through every brick.
        hash_map = collections.Counter()
        for w in wall:
            loc = 0
            for i in range(len(w) - 1):  # We don't want to include the walls.
                loc += w[i]
                hash_map[loc] += 1
        # print(hash_map)
        
        return len(wall) if not hash_map else len(wall) - max(hash_map.values())
        # return len(wall) if not hash_map else len(wall) - max(hash_map, key = hash_map.get)

        

        
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        totv = collections.defaultdict(int)
        vids = collections.defaultdict(list)
        
        for c, i, v in zip(creators, ids, views):
            totv[c] += v
            heapq.heappush(vids[c], (-v, i))
            
        max_v = max(totv.values())
        ans = []
        for c in totv.keys():
            if totv[c] == max_v:
                ans.append([c, vids[c][0][1]])
        return ans
        
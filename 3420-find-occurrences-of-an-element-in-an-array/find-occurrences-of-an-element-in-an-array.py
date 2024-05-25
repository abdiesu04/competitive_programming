class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            if num == x:
                indices.setdefault(num, []).append(i)
        
        answer = []
        for query in queries:
            if x not in indices or query > len(indices[x]):
                answer.append(-1)
            else:
                answer.append(indices[x][query - 1])
        
        return answer
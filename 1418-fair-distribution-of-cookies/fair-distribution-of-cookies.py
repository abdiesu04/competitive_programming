class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_distribution = float('inf')
        cookies.sort(reverse=True)
        def backtrack(index, distributions):
            nonlocal min_distribution
            
            if index == len(cookies):
                current_max = max(distributions)
                min_distribution = min(min_distribution, current_max)
                return

            current_max = max(distributions)
            if current_max >= min_distribution:
                return
                
            for i in range(k):
                distributions[i] += cookies[index]
                
                backtrack(index + 1, distributions)
                
                distributions[i] -= cookies[index]

        distributions = [0] * k
        backtrack(0, distributions)
        return min_distribution

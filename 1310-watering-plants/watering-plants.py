class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        can = capacity
        for i, x in enumerate(plants): 
            if can < x: 
                ans += 2*i
                can = capacity
            ans += 1
            can -= x
        return ans 
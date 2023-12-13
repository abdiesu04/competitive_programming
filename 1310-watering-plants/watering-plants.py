class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        moves = 0
        water = capacity
        for i in range(len(plants)):
            if water < plants[i]:
                moves += 2 * i
                water = capacity
            moves += 1
            water -= plants[i]
            
        return moves
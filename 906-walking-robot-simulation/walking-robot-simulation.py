class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert obstacles list to a set for fast lookup
        obst_set = set(map(tuple, obstacles))
        
        # Directions: north (+y), east (+x), south (-y), west (-x) 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial state
        x, y = 0, 0  # Starting position 
        dir_idx = 0  # Facing north initially 
        max_distance_sq = 0  # Keep track of the max distance squared 
        
        for command in commands:
            if command == -1:  # Turn right 
                dir_idx = (dir_idx + 1) % 4
            elif command == -2:  # Turn left 
                dir_idx = (dir_idx - 1) % 4
            else:  # Move forward \U0001f6b6‍♂️
                dx, dy = directions[dir_idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obst_set:  # Check if the next step is free of obstacles 
                        x += dx  # Move in the x direction 
                        y += dy  # Move in the y direction 
                        # Update the maximum distance squared 
                        max_distance_sq = max(max_distance_sq, x ** 2 + y ** 2)
                    else:
                        break  # Stop if the next step is an obstacle 
        
        return max_distance_sq  # Return the maximum distance squared 
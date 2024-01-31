class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # Sort g & s
        g.sort()
        s.sort()
        
        # Set child to zero
        child = 0
        
        # Loop over s(cookies)
        for cookie in s:
            
            # If child greed satisfy
            if cookie >= g[child]:
                
                # Then increment child
                child += 1
                
            # If no child left
            if child == len(g):
                
                # Then return child
                return child
        
        # Return child
        return child
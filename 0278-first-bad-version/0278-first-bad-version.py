# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Initialize pointers low and high to the first and last version numbers respectively
        low, high = 1, n
        # Initialize mid to the middle version number
        mid = (high + low) // 2
        
        # While low pointer is not greater than high pointer 
        while (low<= high):
            # If the current version (mid) is bad
            if isBadVersion(mid):
                # Check if the previous version (mid-1) is not bad. 
                #If it is not bad, then mid is the first bad version
                if not isBadVersion(mid-1):
                    return mid
                # If the previous version (mid-1) is bad, 
                #then the first bad version must be in the range [low, mid-1]. So, update high to mid-1
                high = mid - 1
                # If the current version (mid) is not bad
            else:
                # Check if the next version (mid+1) is bad. If it is bad, 
                #then mid+1 is the first bad version
                if isBadVersion(mid+1):
                    return mid+1
                # If the next version (mid+1) is not bad, 
                #then the first bad version must be in the range [mid+1, high]. So, update low to mid+1
                low = mid + 1
            
            # Recalculate mid based on the updated values of low and high
            mid = (high + low) // 2
        
        # If the loop exits, it means that there are no bad versions in the given range, so return -1
        return -1
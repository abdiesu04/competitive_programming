#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
            
            # Brute Force
            # if x < 0:
            #     x = -x
            #     x = int(str(x)[::-1])
            #     x = -x
            # else:
            #     x = int(str(x)[::-1])
            # 
            # if x < -2**31 or x > 2**31 - 1:
            #     return 0
            # else:
            #     return x
    
            # Math
            # if x < 0:
            #     x = -x
            #     x = int(str(x)[::-1])
            #     x = -x
            # else:
            #     x = int(str(x)[::-1])
            # 
            # if x < -2**31 or x > 2**31 - 1:
            #     return 0
            # else:
            #     return x
    
            # Math (Optimized)
            if x < 0:
                x = -x
                x = int(str(x)[::-1])
                x = -x
            else:
                x = int(str(x)[::-1])
            
            if x < -2**31 or x > 2**31 - 1:
                return 0
            else:
                return x
    
            # Math (Optimized)
            # if x < 0:
            #     x = -x
            #     x = int(str(x)[::-1])
            #     x = -x
            # else:
            #     x = int(str(x)[::-1])
            # 
            # if x < -2**31 or x > 2**31 - 1:
            #     return 0
            # else:
            #     return x
    
            # Math (Optimized)
            # if x < 0:
            #     x = -x
            #     x = int(str(x)[::-1])
            #     x = -x
            # else:
            #     x = int(str(x)[::-1])
            # 
            # if x < -2**31 or x > 2**31 - 1:
            #     return 0
            # else:
            #     return x
    
            # Math (Optimized)
            # if x < 0:
            #     x = -x
            #


# @lc code=end


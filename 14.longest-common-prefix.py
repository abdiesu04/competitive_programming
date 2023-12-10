#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]  # Assume the first string as the common prefix
        
        for i in range(1, len(strs)):
            current_str = strs[i]
            j = 0
            
            while j < len(prefix) and j < len(current_str) and prefix[j] == current_str[j]:
                j += 1
            prefix = prefix[:j]  
            if prefix == "":
                break
        
        return prefix
        
# @lc code=end


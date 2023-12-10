#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        st = ""
        
        for i in sorted(dic.items(), key=lambda x:x[1]):
           
            st += i[0] * i[1]
        
        return st[::-1]
        
# @lc code=end


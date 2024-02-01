class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
    	### convert nums to set.
        Set = set(nums)
        for n in nums:
            strN = str(n) 		### convert n to string
            strR = strN[::-1] 	### reverse the digits
            Set.add(int(strR))	### add it to set
        ### just return the length of the set
        return len(Set)
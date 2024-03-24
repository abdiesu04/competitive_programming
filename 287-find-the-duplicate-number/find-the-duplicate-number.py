class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0 , 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
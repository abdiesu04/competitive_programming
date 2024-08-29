class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s , low , high):
            if low >= high:
                return
            s[low] , s[high] = s[high] , s[low]

            reverse(s , low + 1 , high -1)

        reverse(s , 0 , len(s) - 1)

             
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        m = '../'
        r = './'

        stack = []

        for i in logs:
            if (i == m):
                if(len(stack) > 0):
                    stack.pop()
            elif i == r:
                continue
            else:
                stack.append(i)
        return len(stack)



        
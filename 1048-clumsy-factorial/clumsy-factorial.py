class Solution:
    def clumsy(self, n: int) -> int:
        operations = ["*" , "/" , "+" , "-"]
        stack = [n]

        for i in range(n-1):
            # print(stack)
            op = operations[(i)%4]
            # print(op , n-i-1)
            if op == "*":
                stack.append((n-i-1) * stack.pop())
            elif op == "/":
                stack.append(int(stack.pop() / (n-i-1) ))
            elif op == "+":
                stack.append(n-i-1)
            else:
                stack.append(-(n-i-1))

        res = 0
        for i in range(len(stack)):
            res += stack[i]
        return res
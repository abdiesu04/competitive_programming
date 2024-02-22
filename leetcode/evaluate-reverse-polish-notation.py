class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                stack.append(int(i))
            else:
                if len(stack) > 1:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if i == '+':
                        res = num1 + num2
                    elif i == '-':
                        res = num2 - num1
                    elif i == '/':
                        res = num2 / num1
                    else:
                        res = num1 * num2
                    stack.append(int(res))


        return stack.pop()
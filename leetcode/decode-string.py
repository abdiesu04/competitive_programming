class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]

        for c in s:
            if c!=']':
                stack.append(c)
            else:
                res=''
                while stack[-1]!='[':
                    res+=stack.pop()
                stack.pop()
                n=''
                while len(stack)!=0 and stack[-1].isdigit()==True:
                    n+=stack.pop()
                stack.append(res*int(n[::-1]))

        return ''.join([word[::-1] for word in stack])


    
        
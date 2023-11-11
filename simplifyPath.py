class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path
        stack = []
        for s in path.split("/"):
            if s == "..":
                if len(stack)>0:
                    stack.pop()
            elif s == "." or not s:
                continue
            else:
                stack.append(s)
        return "/" + "/".join(stack)

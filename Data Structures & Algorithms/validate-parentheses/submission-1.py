class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        oc={")":"(","}":"{","]":"["}
        for c in s:
            if c in oc:
                if stack and stack[-1]==oc[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
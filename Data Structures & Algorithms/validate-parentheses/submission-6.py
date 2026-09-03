class Solution:
    def isValid(self, s: str) -> bool:
        b={')':'(',']':'[','}':'{'}
        stack=[]
        for ch in s:
            if ch in b:
                if stack:
                    if b[ch]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
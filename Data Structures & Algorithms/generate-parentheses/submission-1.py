class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]        
        ans=[]
        def check(openn,closen):
            if openn==closen==n:
                ans.append("".join(stack))
                return
            if openn<n:
                stack.append('(')
                check(openn+1,closen)
                stack.pop()
            if closen<openn:
                stack.append(')')
                check(openn,closen+1)
                stack.pop()
        check(0,0)
        return ans

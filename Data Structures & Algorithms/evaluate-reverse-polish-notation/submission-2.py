class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]
        val=0
        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                b=stack.pop()
                a=stack.pop()
                if ch=="+":
                    val=a+b
                    stack.append(val)
                elif ch=="-":
                    val=a-b
                    stack.append(val)
                elif ch=="*":
                    val=a*b
                    stack.append(val)
                elif ch=="/":
                    val=a/b
                    stack.append(int(val))
        return stack[0]

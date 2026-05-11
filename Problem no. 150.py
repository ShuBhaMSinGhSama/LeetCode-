class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={"+": lambda a,b:a+b,
            "-": lambda a,b:b-a,
            "*": lambda a,b:a*b,
            "/": lambda a,b:int(b/a)}
        ans=[]
        for i in tokens:
            if i in op:
                a=ans.pop()
                b=ans.pop()
                ans.append(op[i](a,b))
            else:
                ans.append(int(i))
        return ans[0]
        

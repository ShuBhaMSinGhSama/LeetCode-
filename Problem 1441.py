class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        result=[]
        for i in range(1,n+1):
            stack.append(i)
            result.append("Push")
            if target==stack:
                break
            if i not in target:
                stack.pop()
                result.append("Pop")
        return result
            
        

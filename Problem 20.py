class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hmap={'}':'{', ')':'(', ']':'['}
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in hmap:
                if not stack:
                    return False
                q=stack.pop()
                if hmap[i]!=q:
                    return False
        return len(stack) == 0

        

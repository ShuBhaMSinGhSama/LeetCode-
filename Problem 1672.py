class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for i in accounts:
            x=sum(i)
            if x>richest:
                richest =x
        return richest
        

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        
        if low % 2 == 0 and high % 2 == 0:
            return total // 2
        elif low % 2 == 1 and high % 2 == 1:
            return total // 2 + 1
        else:
            return total // 2

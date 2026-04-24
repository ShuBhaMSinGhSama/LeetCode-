class Solution:
    def countDigits(self, num: int) -> int:
        l=[int(i) for i in str(num)]
        count=0
        for i in l:
            if num%i==0:
                count+=1
        return count
        

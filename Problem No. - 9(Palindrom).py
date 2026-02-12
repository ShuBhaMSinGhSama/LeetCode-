class Solution:
    def isPalindrome(self, x: int) -> bool:

        num=x
        r=0
        while num>0:
            z=num%10
            r= r*10+z
            num=num//10
        return(r==x)

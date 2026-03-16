#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(s.lower() for s in s if s.isalnum())
        i= len(s)-1
        x=""
        while i>=0:
            x+=s[i]
            i-=1
        if x==s:
            return(True)
        else:
            return(False)

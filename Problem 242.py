#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r={}
        q={}
        for char in s:
            r[char]=r.get(char,0)+1
        for char in t:
            q[char]= q.get(char,0)+1
        if r==q:
            return True
        else:
            return False

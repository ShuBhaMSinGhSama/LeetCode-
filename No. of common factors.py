#leetcode question link: https://leetcode.com/problems/number-of-common-factors/
#Given two positive integers a and b, return the number of common factors of a and b.

def commonFactors(self, a: int, b: int) -> int:
        r1=[]
        r2=[]

        for i in range(1,int(sqrt(a))+1):
            if a%i==0:
                r1.append(i)
                if a//i !=i:
                    r1.append(a//i)
        for i in range(1,int(sqrt(b))+1):
             if b%i==0:
                r2.append(i)
                if b//i !=i:
                    r2.append(b//i)
        common= len(list(set(r1).intersection(r2)))
        return(common)

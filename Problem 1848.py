#Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. 
#Note that abs(x) is the absolute value of x.
#Return abs(i - start).
#It is guaranteed that target exists in nums

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        x=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                c=abs(i-start)
                if c<x:
                    x=c
        return x

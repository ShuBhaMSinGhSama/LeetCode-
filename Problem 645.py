#You are given an integer array nums representing the data status of this set after the error.
#Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x=-1
        y=-1
        for a in nums:
            index =abs(a)-1
            if nums[index]<0:
                x=abs(a)
            else:
                nums[index]=-nums[index]
        for i in range(len(nums)):
            if nums[i]>0:
                y=i+1

        return[x,y]
                
        
            

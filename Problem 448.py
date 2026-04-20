class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d=[]
        for a in nums:
            index =abs(a)-1
            if nums[index]>0:
                nums[index]=-nums[index]
        for z in range(len(nums)):
            if nums[z] >0:
                d.append(z+1)
        return(d)

    

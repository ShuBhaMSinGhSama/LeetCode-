class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        output=[]
        for i in nums:
            c+=i
            output.append(c)
        return output

        

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        l=1
        r=1
        for i in nums:
            output.append(l)
            l*=i
        for i in range(len(nums)-1,-1,-1):
            output[i]=output[i]*r
            r*=nums[i]
        return(output)

        

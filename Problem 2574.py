class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        leftsum=0
        ans=[]
        for i in nums:
            rightsum=total-i-leftsum
            ans.append(abs(leftsum-rightsum))
            leftsum+=i
        return ans

        

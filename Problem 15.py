class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result =[]
        nums.sort()

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if x==0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif x<0:
                    j+=1
                else:
                    k-=1
        return result

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap={}
        for i, num in enumerate(numbers):
            ans=target-num
            if ans in hmap:
                return(hmap[ans]+1,i+1)
            hmap[num]=i

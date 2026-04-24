class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=-1
        i=0
        j=len(height)-1
        while i<j:
            if height[i]<height[j]:
                area=height[i]*(j-i)
                if max_area<area:
                    max_area=area
                i+=1
            else:
                area=height[j]*(j-i)
                if max_area<area:
                    max_area=area
                j-=1
        return max_area
        

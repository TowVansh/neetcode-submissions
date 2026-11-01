class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        for i in range(0,len(heights)):
            right=len(heights)-1
            minimum=min(heights[right],heights[i])
            thisarea=minimum * (right-i)
            if thisarea>area:
                print(heights[i],heights[right],right-1)
                area=thisarea
                right-=1
        return area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        area=0
        for left in range(0,len(heights)):
            minimum=min(heights[right],heights[left])
            thisarea=minimum * (left-right)
            if thisarea>area:
                area=thisarea
                right+=1
                print(heights[right],heights[left],left-right)
            
        return area
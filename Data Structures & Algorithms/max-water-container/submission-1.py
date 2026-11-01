class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=0
        left=len(heights)-1
        area=0
        for i in range(0,len(heights)):
            minimum=min(heights[right],heights[left])
            thisarea=minimum * (left-right)
            if thisarea>area:
                area=thisarea
                right+=1
                print(right,left)
            
        return area
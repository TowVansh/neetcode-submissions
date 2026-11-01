class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        m_a = 0
        while left < right:
            width = right - left
            c_h = min(heights[left], heights[right])
            area = width * c_h
            m_a = max(m_a, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return m_a
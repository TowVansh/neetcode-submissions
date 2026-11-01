class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        m_a = 0
        maxHeight = max(heights)
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            m_a = max(m_a, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            if m_a >= maxHeight * (right - left):
                break
        return m_a
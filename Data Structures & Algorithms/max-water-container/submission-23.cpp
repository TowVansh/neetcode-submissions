class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int m_a = 0;
        int maxHeight = *max_element(heights.begin(), heights.end());
        while (left < right) {
            int area = min(heights[left], heights[right]) * (right - left);
            m_a = max(m_a, area);
            if (heights[left] <= heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
            if (m_a >= maxHeight * (right - left)) {
                break;
            }
        }
        return m_a;
    }
};
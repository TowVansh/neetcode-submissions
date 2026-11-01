impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = heights.len() - 1;
        let mut m_a = 0;
        let max_height = *heights.iter().max().unwrap();
        while left < right {
            let area = heights[left].min(heights[right]) * (right - left) as i32;
            m_a = m_a.max(area);
            if heights[left] <= heights[right] {
                left += 1;
            } else {
                right -= 1;
            }
            if m_a >= max_height * (right - left) as i32 {
                break;
            }
        }
        m_a
    }
}
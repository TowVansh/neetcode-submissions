class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        e=len(nums)
        for i in range(0,e):
            nums.append(nums[i])
        return nums

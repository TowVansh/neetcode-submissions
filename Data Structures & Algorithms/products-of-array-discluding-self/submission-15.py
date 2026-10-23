class Solution:
    def productExceptSelf(self, nums):
        zeros = nums.count(0)
        p = 1
        for x in nums:
            if x: p *= x
        if zeros > 1: return [0] * len(nums)
        if zeros == 1: return [p if x == 0 else 0 for x in nums]
        return [p // x for x in nums]
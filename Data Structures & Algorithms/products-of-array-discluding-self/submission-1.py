class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        e=1
        f=0
        output=[]
        for i in nums:
            e*=i
            f+=1
        for i in range(f):
            output[i]=e/nums[i]
        return output
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        f=len(nums)
        ans=[]
        for i in range(0,f):
            if i>0 and nums[i]==nums[i-1]:
                continue
            right=f-1
            left=i+1
            target=-nums[i]
            while right>left:
                if nums[right]+nums[left]+target==0:
                    ans.append([nums[i],nums[right],nums[left]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
                elif nums[right]+nums[left]>target:
                    right=right-1
                else:
                    left=left+1
        return ans
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        f=len(nums)
        ans=[]
        for i in range(0,f):
            right=f-1
            left=i+1
            target=nums[i]
            while right>left:
                if nums[right]+nums[left]+target==0 and not (i==right or left==i):
                    ans.append([nums[i],nums[right],nums[left]])
                    break
                elif nums[right]+nums[left]>target:
                    right=right-1
                else:
                    left=left+1
        return ans
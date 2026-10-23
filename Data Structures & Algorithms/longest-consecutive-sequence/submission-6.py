class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        maxi=1
        i=0
        for i in range(len(nums)-1):
            n=1
            for j in range(i+1,len(nums)):
                if(nums[j-1]-1==nums[j] or nums[j-1]==nums[j]):
                    if(nums[j-1]==nums[j]):
                        continue
                    n+=1
                    if maxi<n:
                        maxi=n
                else:
                    i=j
                    break
        return maxi
            

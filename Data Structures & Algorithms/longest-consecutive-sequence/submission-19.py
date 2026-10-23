class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        done=set()
        maxi=1
        if not nums:
            return 0
        for i in nums:
            ref=i
            e=1
            while i+1 in nums and ref not in done:
                e+=1
                done.add(i+1)
                i+=1
            if e>maxi:
                maxi=e
        return maxi
            

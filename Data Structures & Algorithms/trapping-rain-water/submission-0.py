class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        suffix=[]
        maxi=0
        maxii=0
        for i in range(0,len(height)):
            if height[i]>maxi and maxii!=i:
                maxii=i
                maxi=height[i]
            prefix.append(maxi)
        j=len(height)-1
        maxi=0
        maxii=0
        while j>=0:
            if height[j]>maxi and maxii!=i:
                maxii=i
                maxi=height[j]
            suffix.append(maxi)
            j-=1
        ans=[]
        for i in range(0,len(height)):
            ans.append(min(prefix[i], suffix[i]) - height[i])
        return sum(ans)
'''class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        suffix=[]
        maxi=0
        for i in range(0,len(height)):
            if height[i]>maxi:
                maxi=height[i]
            prefix.append(maxi)
        j=len(height)-1
        maxi=0
        while j>=0:
            if height[j]>maxi:
                maxi=height[j]
            suffix.append(maxi)
            j-=1
        suffix.reverse()
        ans=[]
        for i in range(0,len(height)):
            ans.append(min(prefix[i], suffix[i]) - height[i])
        return sum(ans)'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        p = height.index(max(height))
        w = cur = 0
        for h in height[:p]:
            if h < cur:
                w += cur - h
            else:
                cur = h
        cur = 0
        for h in height[:p:-1]:
            if h < cur:
                w += cur - h
            else:
                cur = h
        return w
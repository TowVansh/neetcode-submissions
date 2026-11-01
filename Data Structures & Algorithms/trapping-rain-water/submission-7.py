'''class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        suffix=[]
        maxi=0
        maxii=0
        for i in range(0,len(height)):
            if height[i]>maxi:
                maxii=i
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
        if len(height) < 3:
            return 0
        left = 0
        right = len(height) - 1
        l_m = height[left]
        r_m = height[right]
        w = 0
        while left < right:
            if l_m < r_m:
                left += 1
                h = height[left]
                if h > l_m:
                    l_m = h
                else:
                    w += l_m - h
            else:
                right -= 1
                h = height[right]
                if h > r_m:
                    r_m = h
                else:
                    w += r_m - h
        return w
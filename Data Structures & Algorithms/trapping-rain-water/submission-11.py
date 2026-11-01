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

import numpy as np
from array import array

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        a = np.frombuffer(array("q", height), dtype=np.int64)
        p = int(a.argmax())
        acc = np.maximum.accumulate
        return int(acc(a[:p]).sum() + acc(a[:p:-1]).sum() + a[p] - a.sum())
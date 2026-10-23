class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        e=1
        f=0
        withoutzero=1
        zerocame=0
        output=[]
        for i in nums:
            e*=i
            f+=1
            if not zerocame and i==0:
                zerocame=1
                continue
            else:
                withoutzero*=i
        if e!=0:
            if withoutzero==0:
                output=[0]*f
            else:
                for i in range(f):
                    output.append(int(e/nums[i]))
        else:
            for i in range(f):
                if nums[i]==0:
                    output.append(int(withoutzero))
                    continue
                output.append(int(e/nums[i]))
        return output
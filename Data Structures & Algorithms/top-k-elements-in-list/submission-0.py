class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            if nums.count(n) not in d:
                d[nums.count(n)]=set()
            d[nums.count(n)].add(n)
        maximum=list(d.keys())
        maximum=sorted(maximum,reverse=True)
        ans=[]
        for i in range(0,k):
            for j in d[maximum[i]]:
                ans.append(j)
        return ans
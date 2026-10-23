class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        freq = {}
        for n in d:
            if d[n] not in freq:
                freq[d[n]] = set()
            freq[d[n]].add(n)

        maximum = sorted(freq.keys(), reverse=True)
        ans = []
        for i in range(min(k, len(maximum))):
            for j in freq[maximum[i]]:
                ans.append(j)
                if len(ans) >= k:
                    return ans
        return ans
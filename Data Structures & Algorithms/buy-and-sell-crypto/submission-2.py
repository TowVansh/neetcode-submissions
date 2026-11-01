class Solution:
    def maxProfit(self, price: List[int]) -> int:
        profit=0
        for i in range(len(price)-1):
            if(price[i]<price[i+1]):
                profit+=price[i+1]-price[i]
        return profit
class Solution:
    def maxProfit(self, price: List[int]) -> int:
        profit=0
        for i in range(1,len(price)):
            if(price[i-1]<price[i]):
                profit+=price[i]-price[i-1]
        return profit
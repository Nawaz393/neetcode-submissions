class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buy=prices[0]
        for price in prices:
            profit=price-buy
            buy=min(price,buy)
            maxProfit=max(profit,maxProfit)


        return max(maxProfit,0)
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        max_profit = 0
        for price in prices:
            if price - bought > max_profit:
                max_profit = price - bought
            
            if bought > price:
                bought = price
        return max_profit
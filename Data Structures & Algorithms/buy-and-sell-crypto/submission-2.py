class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        bought = prices[0]
        for price in prices:
            profit = max(profit, price - bought)
            bought = min(price, bought)
        return profit

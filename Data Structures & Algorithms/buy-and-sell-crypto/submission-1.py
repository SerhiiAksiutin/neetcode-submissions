class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for today_price in prices:
            max_profit = max(max_profit, today_price - min_buy)
            min_buy = min(min_buy, today_price)
        return max_profit


        
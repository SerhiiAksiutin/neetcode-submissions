class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            buy, sell = prices[l], prices[r]
            if buy < sell:
                max_profit = max(max_profit, sell - buy)
                r += 1
            else:
                l = r
                r += 1
        return max_profit
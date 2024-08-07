class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(len(prices)):
            if i < len(prices) - 1 and prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit

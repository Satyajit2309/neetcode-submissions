class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in prices:
            minPrice = min(minPrice , i)
            profit = i - minPrice

            maxProfit = max(maxProfit , profit)

        return maxProfit
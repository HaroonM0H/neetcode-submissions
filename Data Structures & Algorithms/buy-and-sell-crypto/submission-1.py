class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        buy = prices[0]

        for i in prices:
            buy = min(buy, i)
            maxPrice = max(maxPrice, i - buy)
        return maxPrice
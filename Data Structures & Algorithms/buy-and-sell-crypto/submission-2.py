class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cheapest = prices[0]
        best = 0

        for price in prices:

            profit = price - cheapest
            best = max(best, profit)

            cheapest = min (cheapest, price)

        return best
        
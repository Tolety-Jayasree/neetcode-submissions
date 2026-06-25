class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minValue=prices[0]
        for num in prices:
            diff= num-minValue
            profit=max(diff,profit)
            minValue=min(num,minValue)
        return profit
        
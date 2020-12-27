class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy search
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += (prices[i] - prices[i-1])
                # print(profit)
        
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # greedy search
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i]>prices[i-1]:
        #         profit += (prices[i] - prices[i-1])
        #         # print(profit)
        
        # return profit

        ## DP
        # f(i): max profit for 0~i
        # f(i) = f(i-1) + max(0, prices[i]-prices[i-1])
        # if len(prices) <= 1:
        #     return 0
        
        pre = 0
        for i in range(1, len(prices)):
            pre = pre + max(0, prices[i] - prices[i-1])
        
        return pre


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## DP
        # f(i): maxprofit for 0~i day
        # f(i) = max(f(i-1), prices(i)-min(price[:i-1])
        if len(prices) <= 1:
            return 0
        pre, minma = 0, prices[0]
        for i in range(1, len(prices)):
            pre = max(pre, prices[i]-minma)
            if prices[i] < minma:
                minma = prices[i]
        
        return pre
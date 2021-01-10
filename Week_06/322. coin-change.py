class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## DP 原始思路
        # f(i) = min(f(i-1), f(i-2), f(i-5)) + 1
        # f(i): min coins for amount i

        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            tem = []
            for coin in coins:
                if coin <= i:
                    tem.append(dp[i-coin])
            if tem:
                dp[i] = min(tem)+1
        
        # print(dp)
        
        return dp[-1] if dp[-1] < amount+1 else -1
        

## international 
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf') # 
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
        

                    



class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        if n <= 2:
            return n
        l = 1
        r = 2
        for _ in range(3, n+1):
            l, r = r, r+l
        
        return r
        ###############################################
        # 3种步长 f(n) = f(n-1) + f(n-2) + f(n-3)
        # 相邻不能重复步长， 暂时不会
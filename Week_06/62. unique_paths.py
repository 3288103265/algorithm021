class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## math: C(m-1, m+n-2)

        ## DP 
        # f(i,j): (0,0)-->(i,j)  num of paths
        # f{i,j} = f(i-1, j) + f(i, j-1)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 1
                elif i==0: 
                    dp[i][j] += dp[i][j-1]
                elif j==0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1] 

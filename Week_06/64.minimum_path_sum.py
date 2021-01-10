class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ## 暴力法：（m-1）个下，（n-1）个右，向下和向右的排列。通过选择数计算出C（m-1， m+n-2）

        ## 递归， DFS， BSF

        ## DP bottom-up
        #f（i，j）表示到右下角的最小路径和。
        # dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i, j]
        
        # m, n = len(grid), len(grid[0])
        # dp = grid
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i==m-1 and j==n-1:
        #             continue
        #         if i==m-1:
        #             dp[i][j] = dp[i][j]+dp[i][j+1]
        #         elif j == n-1:
        #             dp[i][j] = dp[i][j]+dp[i+1][j]
        #         else:
        #             dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        # # print(dp)
        # return dp[0][0]

        ## dp top-down
        # f(i,j)表示到左上角的最小路径和
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: 
                    continue
                if j==0: 
                    grid[i][j] += grid[i-1][j]
                elif i==0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## dp bottom-up：f[i][j]表示三角形从底部走到（i，j）的最小路径
        # pro(i,j) is min length path of i,j. pro(i,j)=min(sub(i+1,j), sub(i+1, j+1))+a(i,j)
        a = triangle
        for i in range(len(a)-2, -1, -1):
            for j in range(i+1):
                a[i][j] += min(a[i+1][j], a[i+1][j+1])
        print(a)
        
        return a[0][0]
        
        
        ## dp top-down
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
     
        ## 2. DFS
        left = right = n
        cur_res = ""
        ans = []

        def dfs(cur_res, left, right): # number of left and right.
            if left ==0 and right == 0:
                ans.append(cur_res)
                return 
            if left > right: # the number of left must be greater than the 
                return
            if left > 0: # use a left 
                dfs(cur_res+'(',left-1, right)
            if right > 0: # use a right
                dfs(cur_res+')', left, right-1)
        
        dfs(cur_res, n, n)
        return ans
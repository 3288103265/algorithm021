class Solution:
    def numDecodings(self, s: str) -> int:
        ## BFS/DFS? 剪枝

        ## DP
        # f(i): s[:i] decode ways
        # f(i) = f(i-1)*(如果si在字典，为1，否则为0) + f(i-2)*(如果后两个字母组成的字符串在字典里为1))
        dic = {num:char for num, char in enumerate('abcdefghigklmnopqrstuvwxyz',1)}
        print(dic)
        def decode(s):
            return dic[s] if s in dic else 0
        if len(s)==1:
            dic[s] if s in dic else 0

        
        
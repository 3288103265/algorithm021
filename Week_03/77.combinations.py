class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # recursive
        # terminator

        if n<k or n<1 or k<0:
            return []
        if k==0:
            return [[]]
        if n == k:
            return [list(range(1,n+1))]

        # process & drill down:
        # C(n-1,K)
        # C(n-1,k-1) append elem n
        return self.combine(n-1, k) + [item+[n] for item in self.combine(n-1, k-1)] ## 
       



        

        
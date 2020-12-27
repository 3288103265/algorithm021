class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # binary search
        if num <= 0:
            return False
        l = 0
        r = num
        while l<=r:
            mid = (l+r)//2
            if mid*mid < num:
                l = mid+1
            elif mid*mid >num:
                r = mid-1
            else:
                return True
        
        return False
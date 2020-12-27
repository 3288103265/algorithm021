class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        l = 0
        r = x
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    

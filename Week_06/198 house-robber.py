class Solution:
    def rob(self, nums: List[int]) -> int:
        ## dp
        # f(i) = max(nums[k]+f(k-2), f(k-1))
        # f(i):到房子i时获得的最高金额
        dp = nums
        if not dp:
            return 0
        print(nums)
        if len(nums)==1:
            return dp[0]
        if len(nums)==2:
            return max(dp)
        dp[1] = max(dp[:2]) 
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1] ## 可以进一步用滚动数组优化

## dp International
class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
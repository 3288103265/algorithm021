class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## brute-force. )(n^2)
        ## DP
        # f(i)表示包含了nums[i]的最大子子序和。
        # f(i) = max(f(i-1)+nums[i], nums[i])。 带上f(i-1)或者从头开始计算。

        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], 0) + nums[i]
        
        return max(dp)
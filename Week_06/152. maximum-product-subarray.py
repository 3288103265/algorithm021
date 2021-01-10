## https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## brute-force n^2

        ## DP
        
        # g(i)表示包含了元素nums[i]的最小子序积
        # g(i)= min(g(i-1))*nums[i], f(i-1)*nums[i], nums[i])
        # f(i)表示包含了元素nums[i]的最大子序积
        # f(i) = max(f(i-1)*num[i], nums[i], g(i-1)*nums[i]), 考虑负负得正

        dp1 = nums
        dp2 = dp1.copy()
        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
            dp2[i] = min(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])

        print(dp1)
        return max(dp1)
        
        ####g该解法是错误的，原因在于dp1 nums共享内存，当dp1[i]改变时，nums[i]也被改变了，dp2错误
#需要使用copy

        dp1 = nums.copy()
        dp2 = nums.copy()
        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
            dp2[i] = min(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])

        return max(dp1)
        #####################由于只是用了两个状态，可以用两个常量来优化############
        #####################数学，，，
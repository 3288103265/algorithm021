class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力求解
        # ans = []
        # if len(nums)<1:
        #     return -1
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:     
        #             return [i, j]
        
        # return -1


        # 2. hash
        hash_dict = dict()
        for i, num in enumerate(nums):
            if target - num in hash_dict:
                return [hash_dict[target-num], i]
            
            else:
                hash_dict[num] = i 
        
    
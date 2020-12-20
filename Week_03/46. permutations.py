class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursive
        # terminator
        
        if len(nums) <= 1:
            return [nums]
        
        # process & drill down
        
        last_peru = self.permute(nums[:-1])
        # insert nums[:-1] to last_peru
        
        cur_peru = [self._insert(p.copy(), i, nums[-1]) for p in last_peru for i in range(0, len(nums))]
        return cur_peru

    def _insert(self, nums: List[int], ind: int, elem: int) -> List:
        
        nums.insert(ind, elem)
        return nums
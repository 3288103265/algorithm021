## greedy Back
## greedy Forward

[fastest]
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        curr = 0
        next_loc = 0
        count = 0
        for i in range(n):
            # find the max range for each of the n spot.
            if curr<i:
                count+=1
                curr = next_loc
            next_loc = max(next_loc, i+nums[i])
        return count

          
            # return count
## bfs
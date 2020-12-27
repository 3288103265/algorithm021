# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # level traversal& BFS
        # ans = []
        # queue = Deque()
        # if root:
        #     queue.append(root)
        
        # while queue:
        #     level_size = len(queue)
        #     mx = -inf
        #     for i in range(level_size):
        #         node = queue.popleft()
        #         mx = max(node.val, mx)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     ans.append(mx)
        
        # return ans

        ## refer international website most vote answer.
        ## python level traversal
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes

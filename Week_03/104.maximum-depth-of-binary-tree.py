# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # 递归

        #终止条件
        if not root:
            return 0
        
        #process
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
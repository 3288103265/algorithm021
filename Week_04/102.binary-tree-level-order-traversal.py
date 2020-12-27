# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # # BFS queue.
        # ans = []
        # queue = Deque()
        # if root:
        #     queue.append(root)
        # # print(queue)
        
        # # visited.
        # while queue:
        #     level_num = len(queue) # number of nodes in current level.
        #     level_ans = []
        #     for i in range(level_num):
        #         # process current
        #         node=queue.popleft()
        #         level_ans.append(node.val)        
        #         # down
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     # print(level_ans)
        #     ans.append(level_ans)
                    
        # return ans

        # level traversal compact
        levels = []
        row = [root]
        while any(row):
            levels.append([node.val for node in row])
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        
        return levels
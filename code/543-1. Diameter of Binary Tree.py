# using DFS to search Diameter 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def traval_get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = traval_get_depth(node.left)
            right = traval_get_depth(node.right)

            nonlocal best
            best = max(best, left + right)

            return  max(left, right) + 1

        _ = traval_get_depth(root)

        return best

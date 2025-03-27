# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
            
        def travel(node: TreeNode) -> int:
            if not node:
                return 0
            
            left = travel(node.left)
            right = travel(node.right)

            # Update the external variable record as long as one side is unbalanced (the depth difference exceeds 1).
            if abs(left - right) > 1:
                nonlocal result
                result = False

            return max(left, right) + 1
        
        travel(root)

        return result

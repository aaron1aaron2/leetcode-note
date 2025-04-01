# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None) & (q == None):
            return True
        elif (p == None) | (q == None):
            return False
        elif p.val != q.val:
            return False
        else:
            # Both have no NONE and the value is the same, then continue to compare
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
        
        # Make sure the results of the two sides are correct
        return left & right

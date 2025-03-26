# BFS using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.travel(root, 0)

    def travel(self, node: Optional[TreeNode], count: int) -> int:
        if node == None:
            return count

        # traval back from leaf
        left = self.travel(node.left, count)
        right = self.travel(node.right, count)

        count = max(left, right)

        # count current node 
        count += 1

        return count


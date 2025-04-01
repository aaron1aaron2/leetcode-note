# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if (p == None) | (q == None):
                return p == q
            elif p.val != q.val:
                return False
            else:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
            
            return left & right

        # Use BFS to wander and compare sub tree
        from collections import deque 
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if node.val == subRoot.val:
                    result = isSameTree(node, subRoot)
                
                    if result:
                        return True
        
        return False

# implement of DFS using queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque
        q = deque()
        q.append(root)
        
        count = 0
        while q:
            # travel nodes in current layer
            for _ in range(len(q)):
                curr_node = q.popleft()
                # append nodes in next layer
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                
            count += 1
        
        return count

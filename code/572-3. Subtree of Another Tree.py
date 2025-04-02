# Use the hash comparison directly | solution by https://leetcode.com/problems/subtree-of-another-tree/solutions/1130997/Python-or-O(n)-or-super-easy-to-understand/
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def hashify(node):
            if not node:
                return None
            key = (node.val, hashify(node.left), hashify(node.right))

          return memo.setdefault(key, len(memo))
        
        memo = {}
        hashify(s)
        
        return (t.val, hashify(t.left), hashify(t.right)) in memo

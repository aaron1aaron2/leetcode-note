# using list to record passed node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass_node = []
        curr = head
        while curr != None:
            if curr.next in pass_node:
                return True
            pass_node.append(curr)
            curr = curr.next
        
        return False

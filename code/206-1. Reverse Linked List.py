# my solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle the edge case
        if head == None:
            return head
        elif head.next == None:
            return head
        elif head.next.next == None:
            new = head.next
            new.next = head
            head.next = None
            return new

        prev_node = head
        curr = head.next
        while curr.next != None:
            # revert pointer
            next_node = curr.next
            curr.next = prev_node

            # refersh node
            prev_node = curr
            curr = next_node
        
        # Handle the beginning and end 
        head.next = None
        curr.next = prev_node

        return curr

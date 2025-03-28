# using pointer scan two list 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        curr = root

        while (list1 != None) and (list2 != None):
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            
            curr = curr.next

        if list1 == None:
            curr.next = list2
        else:
            curr.next = list1

        return root.next        

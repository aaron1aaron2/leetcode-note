# Recursive Solution by https://leetcode.com/problems/reverse-linked-list/solutions/6072712/video-solution-with-visualization/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

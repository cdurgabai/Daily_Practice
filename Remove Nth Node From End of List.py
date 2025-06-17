# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead to maintain a gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the node
        slow.next = slow.next.next

        return dummy.next

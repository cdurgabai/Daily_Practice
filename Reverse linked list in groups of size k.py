class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def countNodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        node_count = countNodes(head)

        while node_count >= k:
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group = group_end.next
            group_end.next = None
            new_head = reverseLinkedList(group_start, None)
            group_prev.next = new_head
            group_start.next = next_group
            group_prev = group_start
            node_count -= k

        return dummy.next

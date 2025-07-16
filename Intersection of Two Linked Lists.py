class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        
        # Traverse both lists; once a pointer reaches the end, redirect it to the head of the other list.
        # If there's an intersection, they will meet there after at most 2 passes.
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA  # Could be None if no intersection

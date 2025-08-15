import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []

    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" ".join(res))

if __name__ == "__main__":
    k = int(input().strip())
    lists = []
    for _ in range(k):
        data = list(map(int, input().strip().split()))
        n = data[0]
        arr = data[1:]
        lists.append(build_linked_list(arr))
    
    merged_head = mergeKLists(lists)
    print_linked_list(merged_head)

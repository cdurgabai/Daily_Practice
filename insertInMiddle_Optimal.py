class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        if head==None:
            return Node(x)
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        newNode=Node(x)
        front=slow.next
        slow.next=newNode
        newNode.next=front
        return head

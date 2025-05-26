class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        if head==None:
            return Node(x)
        Len=0
        temp=head
        while temp:
            Len+=1
            temp=temp.next
        if Len%2==0:
            prev=None
            slow=head
            fast=head
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            newNode=Node(x)
            prev.next=newNode
            newNode.next=slow
            return head
        else:
            slow=head
            fast=head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            front=slow.next
            newNode=Node(x)
            slow.next=newNode
            newNode.next=front
            return head
        

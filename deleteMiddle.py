# Node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked list creation 
class Solution:
    def constructLL(self, arr):
        # code here
        head=None
        for data in arr:
            if head==None:
                head=Node(data) #Fixed
                temp=head
            else:
                temp.next=Node(data)
                temp=temp.next

        deleteMiddleele=deleteMiddle(head)
        print(deleteMiddleele)

        printLL(head) # To print the nodes

        
# Delete middle
def deleteMiddle(head):
    if head==None or head.next==None:
        return None
    slow=head
    fast=head
    prev=None
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    slow.next=None
    return head
    # return slow.data # To return the deleted ele


def printLL(head):
  temp=head
  while temp:
    print(str(temp.data)+"->"+str(temp.next), end=" ") # To access both
    temp=temp.next
    
arr=list(map(int,input().split())) # 1 2 3 4
s=Solution()
head=s.constructLL(arr)

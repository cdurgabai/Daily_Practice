# Doubly linked list creation
class Node:
    def __init__(self,data):
        self.prev=None
        self.val=data
        self.next=None

def createDLL(arr):
    head=None
    for data in arr:
        if head==None:
            head=Node(data)
            temp=head
        else:
            newNode=Node(data)
            newNode.prev=temp
            temp.next=newNode
            temp=temp.next

arr=[1,2,3]
createDLL(arr)

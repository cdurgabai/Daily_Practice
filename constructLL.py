# P1: Creation of linked list (gfg)

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

        printLL(head) # To print the nodes
def printLL(head):
    temp=head
    while temp:
        # print(temp.data) # To access the value
        # print(temp.next) # To access the address
        print(str(temp.data)+"->"+str(temp.next), end=" ") # To access both
        temp=temp.next
        
    #return head # Returns the head value
    
arr=list(map(int,input().split()))
s=Solution()
head=s.constructLL(arr)

'''
o/p: 1-><__main__.Node object at 0x000002259CEB6DD0> 
2-><__main__.Node object at 0x000002259CEB6E10> 
3-><__main__.Node object at 0x000002259CEB6E50> 
4-><__main__.Node object at 0x000002259CEB6E90> 
5->None 
'''

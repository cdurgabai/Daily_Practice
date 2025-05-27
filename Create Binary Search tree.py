# Create Binary Search tree
class Node:
    def __init__(self,data):
        self.left=None
        self.val=data
        self.right=None
def createBST(arr):
    root=None
    for data in arr:
        if root==None:
            root=Node(data)
        else:
            temp=root
            while True:
                # Smaller elments
                if data<temp.val:
                    if temp.left==None:
                        temp.left=Node(data)
                        break
                    else:
                        temp=temp.left
                # Larger elements
                if data>temp.val:
                    if temp.right==None:
                        temp.right=Node(data)
                        break
                    else:
                        temp=temp.right
    print(root.left.right.val) # 3

arr=[6,2,1,3,9,8,7]
createBST(arr)

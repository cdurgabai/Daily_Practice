 #Maximum Depth of Binary Tree using recursion    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findH(root):
            if root==None:
                return 0
            lh=findH(root.left)
            rh=findH(root.right)
            return 1+max(lh,rh)
        return findH(root)

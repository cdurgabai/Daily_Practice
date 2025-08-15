import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def max_sum_no_adj(node):
    if not node:
        return (0, 0)  

    left_include, left_exclude = max_sum_no_adj(node.left)
    right_include, right_exclude = max_sum_no_adj(node.right)

    include = node.key + left_exclude + right_exclude
    exclude = max(left_include, left_exclude) + max(right_include, right_exclude)

    return (include, exclude)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().strip().split()))
 
        root = None
        for val in arr:
            root = insert(root, val)
        
        include, exclude = max_sum_no_adj(root)
        print(max(include, exclude))

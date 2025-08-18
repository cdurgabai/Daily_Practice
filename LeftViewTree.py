class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def leftView(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)

            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

if __name__ == "__main__":
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N = int(input().strip())
        arr = list(map(int, input().strip().split()))

        root = None
        for val in arr:
            root = insert(root, val)

        res = leftView(root)
        results.append(" ".join(map(str, res)))

    print("\n".join(results))

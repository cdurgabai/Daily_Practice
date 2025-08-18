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

def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.val > n1 and root.val > n2:
        return findLCA(root.left, n1, n2)

    if root.val < n1 and root.val < n2:
        return findLCA(root.right, n1, n2)

    return root

if __name__ == "__main__":
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N, Q = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))

        root = None
        for val in arr:
            root = insert(root, val)
        
        res = []
        for _ in range(Q):
            u, v = map(int, input().strip().split())
            lca = findLCA(root, u, v)
            res.append(str(lca.val))
        
        results.append(" ".join(res))

    print("\n".join(results))

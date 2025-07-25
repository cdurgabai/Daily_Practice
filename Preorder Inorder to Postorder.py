def build_postorder(preorder, inorder):
    index_map = {val: idx for idx, val in enumerate(inorder)}
    
    def helper(preL, inL, inR):
        if preL >= len(preorder) or inL > inR:
            return []
        root = preorder[preL]
        idx = index_map[root]
        left_size = idx - inL
        left = helper(preL + 1, inL, idx - 1)
        right = helper(preL + 1 + left_size, idx + 1, inR)
        return left + right + [root]
    
    return helper(0, 0, len(inorder) - 1)

T = int(input())
for _ in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = build_postorder(preorder, inorder)
    print(' '.join(map(str, postorder)))


"""
3
7
1 2 4 5 3 6 7
4 2 5 1 6 3 7
10
8 5 9 7 1 12 2 4 11 3
9 5 1 7 2 12 8 4 3 11
9
2 7 3 6 8 11 5 9 4
3 7 8 6 11 2 5 4 9

4 5 2 6 7 3 1
9 1 2 12 7 5 3 11 4 8
3 8 11 6 7 4 9 5 2
"""
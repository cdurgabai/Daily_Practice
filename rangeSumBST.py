class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        tot = 0
        st = [root]
        while st:
            x = st.pop()
            if not x:
                continue
            if x.val < low:
                st.append(x.right)
            elif x.val > high:
                st.append(x.left)
            else:
                tot += x.val
                st.append(x.left)
                st.append(x.right)
        return tot

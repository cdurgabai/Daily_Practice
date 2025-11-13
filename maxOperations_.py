class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ans = cnt = 0
        for i in range(n):
            if s[i] == '1':
                cnt += 1
            elif i > 0 and s[i - 1] == '1':
                ans += cnt
        return ans

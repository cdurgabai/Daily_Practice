class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        dp = [[0]*n for _ in range(n)]
        # dp[i][j] = best triangulation between i..j
        for l in range(3, n+1): # length of sub-polygon
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = float('inf')
                for k in range(i+1, j): # try splitting at k
                    dp[i][j] = min(dp[i][j],
                                dp[i][k] + dp[k][j] + v[i]*v[j]*v[k])
        return dp[0][n-1]    

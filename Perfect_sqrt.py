class Solution:
    def floorSqrt(self, n):
        ans = 0
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= n:
                ans = mid
                low = mid + 1
            elif mid * mid > n:
                high = mid - 1
        return ans
n=5
s=Solution()
res=s.floorSqrt(n)
print(res) #2

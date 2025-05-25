class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        squares = set(x*x for x in arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i]**2 + arr[j]**2 in squares:
                    return True
        return False

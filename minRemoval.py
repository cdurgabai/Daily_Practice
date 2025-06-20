import bisect

class Solution:
    # Function to find the minimum number of elements to be removed.
    def minRemoval(self, arr):
        arr.sort()
        n = len(arr)
        min_removals = n  # worst case: remove all

        for i in range(n):
            # Find the rightmost index j such that arr[j] <= 2 * arr[i]
            upper_limit = 2 * arr[i]
            j = bisect.bisect_right(arr, upper_limit)
            length = j - i  # valid subarray length
            min_removals = min(min_removals, n - length)

        return min_removals

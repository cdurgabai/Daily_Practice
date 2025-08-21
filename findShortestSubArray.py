from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            indexes[num].append(i)
        degree = max(len(v) for _, v in indexes.items())
        res = float("inf")
        for l in indexes.values():
            if len(l) == degree:
                res = min(res, l[-1]-l[0]+1)
        return res

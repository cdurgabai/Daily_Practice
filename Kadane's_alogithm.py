# Kadane's alogithm --> Imp
# Maximum Subarray --> TC = O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxS=float("-inf")
        currS=0
        for i in nums:
            currS+=i
            maxS=max(maxS,currS)
            if currS<0:
                currS=0
        return maxS
nums=[-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(nums)) # 6

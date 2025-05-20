class Solution:
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
arr = list(map(int,input().split())) # 1 3 5 6
target=int(input()) # target = 5
S=Solution()
print(S.searchInsert(arr,target)) # 2

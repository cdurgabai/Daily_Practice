class Solution:
    def lowerBound(self, arr, target):
        #code here
        n=len(arr)
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
arr = list(map(int,input().split())) # arr[] = [2, 3, 7, 10, 11, 11, 25]
target=int(input()) # target = 9
S=Solution()
print(S.lowerBound(arr,target)) # 3

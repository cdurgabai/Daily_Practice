class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        l=0
        h=n-1
        Min=float("inf")
        mIndex=-1
        while l<=h:
            mid=(l+h)//2
            if arr[l]<=arr[mid]:
                if arr[l]<Min:
                    Min=arr[l]
                    mIndex=l
                l=mid+1
            if arr[mid]<=arr[h]:
                if arr[mid]<Min:
                    Min=arr[mid]
                    mIndex=mid
                h=mid-1
        return mIndex
            

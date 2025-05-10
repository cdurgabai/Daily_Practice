def findMin(arr):
    low = 0
    high = len(arr)-1
    Min = float("inf")
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            if arr[low]<=Min:
                Min=arr[low]
            low=mid+1
        elif arr[mid]<=arr[high]:
            if arr[mid]<=Min:
                Min=arr[mid]
            high=mid-1
    return Min
arr = list(map(int,input().split()))
print(findMin(arr))
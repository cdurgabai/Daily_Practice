def findOnce(arr):
    n=len(arr)
    if(n==1):
        return arr[0]
    if(arr[0]!=arr[1]):
        return arr[0]
    if(arr[n-1]!=arr[n-2]):
        return arr[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]!=arr[mid-1] and arr[mid] != arr[mid+1]):
            return arr[mid]
        # You are on the left side so the elemnet will be on the right side
        elif((mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1])):
            low=mid+1
        # You are on the right side so the elemnet will be on the left side
        elif((mid%2==1 and arr[mid]==arr[mid+1]) or (mid%2==0 and arr[mid]==arr[mid-1])):
            high=mid-1
arr = list(map(int,input().split()))
print(findOnce(arr)) # 1 1 2 2 3 3 4 50 50 65 65, o/p: 4

def getFloorAndCeil(a, n, x):
    def getFlooor(a,n,x):
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if a[mid]<=x:
                ans=a[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def getCeil(a,n,x):
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if a[mid]>=x:
                ans=a[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
    # Write your code here.
    floor=getFlooor(a,n,x)
    ceil=getCeil(a,n,x)
    return [floor,ceil]

n=int(input())
x=int(input())
a=list(map(int,input().split()))
print(getFloorAndCeil(a,n,x))

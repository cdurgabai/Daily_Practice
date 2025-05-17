def findways(arr,K):
    def check(ind,arr,K):
        if K==0:
            return True
        if K<0 or ind == len(arr):
            return False
        path1=check(ind+1,arr,K-arr[ind])
        path2=check(ind+1,arr,K)
        return path1+path2
    ind=0
    return check(ind,arr,K)

arr=list(map(int,input().split()))
K=int(input())
print(findways(arr,K))

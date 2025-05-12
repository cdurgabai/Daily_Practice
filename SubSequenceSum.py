class Solution:
    def check(self,ind,arr,K):
        if K==0:
            return True
        if K<0 or ind == len(arr):
            return False
        path1=self.check(ind+1,arr,K-arr[ind])
        if path1==True:
            return True
        path2=self.check(ind+1,arr,K)
        return path1 or path2 
    def checkSubsequenceSum(self,arr,K):
        ind = 0
        return self.check(ind,arr,K)
        
arr=list(map(int,input().split()))
K=int(input())
s=Solution()
res=s.checkSubsequenceSum(arr,K)
print(res)

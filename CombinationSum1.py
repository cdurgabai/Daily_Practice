class Solution:
    def generate(self,ind,curr,ans,candi,target):
        if target==0:
            ans.append(curr.copy())
            return
        if target<0 or ind==len(candi):
            return
        curr.append(candi[ind])
        self.generate(ind,curr,ans,candi,target-candi[ind])
        curr.pop()
        self.generate(ind+1,curr,ans,candi,target)
    def combinationSum(self,candi,target):
        ind=0
        curr=[]
        ans=[]
        self.generate(ind,curr,ans,candi,target)
        return ans
    
candi=list(map(int,input().split()))
target=int(input())
s=Solution()
res=s.combinationSum(candi,target)
print(res)

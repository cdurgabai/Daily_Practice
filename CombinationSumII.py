#Combination Sum II(candidate can be used onlt once)
class Solution:
    def generate(self,ind,curr,ans,candi,target):
        if target==0:
            ans.append(curr.copy())
            return
        if target<0 or ind==len(candi):
            return
        curr.append(candi[ind])
        self.generate(ind+1,curr,ans,candi,target-candi[ind])#Take
        curr.pop()
        for i in range(ind+1,len(candi)):
            if candi[ind]!=candi[i]:
                self.generate(i,curr,ans,candi,target) #Not Take
                break
            
    def combinationSum2(self,candi,target):
        candi.sort()
        ind=0
        curr=[]
        ans=[]
        self.generate(ind,curr,ans,candi,target)
        return ans
    
candi=list(map(int,input().split()))
target=int(input())
s=Solution()
res=s.combinationSum2(candi,target)
print(res)

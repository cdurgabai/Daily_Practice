class Solution:
    def generate(self,ind,curr,ans,nums):
        if ind==len(nums):
            ans.append(curr.copy())
            return
        curr.append(nums[ind])
        self.generate(ind+1,curr,ans,nums) #Take
        curr.pop()
        self.generate(ind+1,curr,ans,nums) #Don't Take
        
        
    def subsets(self,nums):
        ind=0 
        ans =[]
        curr=[]
        self.generate(ind,curr,ans,nums)
        return ans

nums=list(map(int,input().split()))
s=Solution()
res=s.subsets(nums)
print(res)

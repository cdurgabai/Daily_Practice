#Combination Sum3
#Input: k=3, n=7
#Output: [[1, 2, 4]]

class Solution:
    def generate(self,k,n,curr,ans):
        if n==0 and len(curr)==k:
            ans.append(curr.copy())
            return
        if n<0 or len(curr)>k:
            return
        if n==0 and len(curr)<k:
            return
        if len(curr)==0:
            ele=1
        else:
            ele=curr[-1]+1
        for i in range(ele,10):
            curr.append(i)
            self.generate(k,n-i,curr,ans)
            curr.pop()
    def combinationSum3(self,k,n):
        curr=[]
        ans=[]
        self.generate(k,n,curr,ans)
        return ans
    
k=int(input())
n=int(input())
s=Solution()
res=s.combinationSum3(k,n)
print(res)

class Solution:
    def generate(self,ind,curr_str,o,c,ans,n):
        if o>n:
            return
        if ind==2*n and o==c:
            ans.append(curr_str)
            return
        self.generate(ind+1,curr_str+"(",o+1,c,ans,n)
        if o>c:
            self.generate(ind+1,curr_str+")",o,c+1,ans,n)
            
    def generateParenthesis(self, n: int):
        ind = 0
        o=0
        c=0
        curr_str=""
        ans=[]
        self.generate(ind,curr_str,o,c,ans,n)
        return ans

n=int(input())
s=Solution()
res=s.generateParenthesis(n)
print(res)

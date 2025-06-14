class Solution:
    def generate(self,ind,curr,ans,digits,combos):
        if(ind==len(digits)):
            ans.append(curr)
            return
        i=int(digits[ind])
        for j in combos[i]:
            self.generate(ind+1,curr+j,ans,digits,combos)
    def letterCombinations(self, digits):
        if(len(digits)==0):
            return[]
        ind=0
        curr=""
        ans=[]
        combos=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.generate(ind,curr,ans,digits,combos)
        return ans

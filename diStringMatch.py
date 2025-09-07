class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        d=len(s)
        ans=[]
        for x in s+'I':
            if x=='D':
                ans.append(d)
                d-=1
            else:
                ans.append(i)
                i+=1
        return ans

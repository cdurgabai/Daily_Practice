class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        maxL=0
        lf=0
        rt=0
        d={}
        while rt<n:
            if fruits[rt] in d:
                d[fruits[rt]]+=1
            else:
                d[fruits[rt]]=1
            if len(d)>2:
                while len(d)>2:
                    d[fruits[lf]]-=1
                    if d[fruits[lf]]==0:
                        del d[fruits[lf]]
                    lf+=1
            maxL=max(maxL,rt-lf+1)
            rt+=1
        return maxL

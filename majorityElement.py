class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        res=[]
        for k,v in d.items():
            if v>n//3:
                res.append(k)
        return res

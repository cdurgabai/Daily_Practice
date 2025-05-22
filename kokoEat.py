# Optimal
from math import*
class Solution:
    def kokoEat(self,arr,k):
        low=1
        high=max(arr)
        while low<=high:
            noOfBananas=(low+high)//2
            time=0
            for num in arr:
                time+=ceil(num/noOfBananas)
            if time<=k:
                high=noOfBananas-1
            else:
                low=noOfBananas+1
        return low
arr=[3,6,7,11]
k=8
s=Solution()
res=s.kokoEat(arr,k)
print(res) # 4

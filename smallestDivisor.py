from math import*
class Solution:
    def smallestDivisor(self, arr, k):
        low=1
        high=max(arr)+1
        while low<=high:
            div=(low+high)//2
            Sum=0
            for num in arr:
                Sum+=ceil(num/div)
            if Sum<=k:
                high=div-1
            else:
                low=div+1
        return low

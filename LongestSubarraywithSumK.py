# P4: Longest Subarray with Sum K
class Solution:
    def longestSubarray(self, arr, k):  
        n=len(arr)
        d={}
        Sum=0
        maxL=0
        for i in range(0,n):
            Sum+=arr[i]
            if Sum==k:
                maxL=i+1
            rem=Sum-k
            if rem in d:
                maxL=max(maxL,i-d[rem])
            if Sum not in d:
                d[Sum]=i 
        return maxL
                
arr=[1,2,3,1,1,1,14,2,3]
k=3
s=Solution()
print(s.longestSubarray(arr,k)) # 3

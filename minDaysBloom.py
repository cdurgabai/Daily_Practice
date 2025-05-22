class Solution:
    def minDaysBloom(self, m, k, arr):
        if m * k > len(arr):
            return -1
        
        low = min(arr)
        high = max(arr)
        ans = -1
        
        while low <= high:
            bloomDay = (low + high) // 2
            count = 0
            noOfBouquets = 0
            
            for flower in arr:
                if flower <= bloomDay:
                    count += 1
                else:
                    noOfBouquets += count // k
                    count = 0
            noOfBouquets += count // k  # process remaining
            
            if noOfBouquets >= m:
                ans = bloomDay
                high = bloomDay - 1
            else:
                low = bloomDay + 1
        
        return ans

m=2
k=3
arr=[7,7,7,7,13,11,12,7]
s=Solution()
res=s.minDaysBloom(m,k,arr)
print(res)

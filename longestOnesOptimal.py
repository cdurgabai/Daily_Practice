#Time Complexity: O(n)
# Space: O(1) 

class Solution:
    def #Time Complexity: O(n)
# Space: O(1) 

class Solution:
    def longestOnes(self,nums,k): #List[int], k: int) -> int:
        n=len(nums)
        maxLen=0
        lf=0
        rt=0
        zero_count=0
        while rt<n:
            if nums[rt]==0:
                zero_count+=1
            if zero_count>k:
                while zero_count>k:
                    if nums[lf]==0:
                        zero_count-=1
                    lf+=1
            maxLen=max(maxLen,rt-lf+1)
            rt+=1
        return maxLen
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
s=Solution()
print(s.longestOnes(nums,k)) # 6



(self,nums,k): #List[int], k: int) -> int:
        n=len(nums)
        maxLen=0
        lf=0
        rt=0
        zero_count=0
        while rt<n:
            if nums[rt]==0:
                zero_count+=1
            if zero_count>k:
                while zero_count>k:
                    if nums[lf]==0:
                        zero_count-=1
                    lf+=1
            maxLen=max(maxLen,rt-lf+1)
            rt+=1
        return maxLen
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
s=Solution()
print(s.longestOnes(nums,k)) # 6




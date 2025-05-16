class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=set()
        n=len(nums)

        for i in range(0,n-1):
            hashmap=[]
            for j in range(i+1,n):
                k=-(nums[i]+nums[j])
                if k in hashmap:
                    temp=[nums[i],nums[j],k]
                    temp.sort()
                    triplets.add(tuple(temp))
                hashmap.append(nums[j])
        ans=[]
        for triplet in triplets:
            ans.append(triplet)
        return ans

# P1: Fruit Into Baskets
# Bruth force solution
# TC= O(N**2) And SC= O(1)
class Solution:
    def totalFruit(self, fruits):# List[int]) -> int:
        n=len(fruits)
        maxL=0
        for i in range(0,n):
            s=set()
            for j in range(i,n):
                s.add(fruits[j])
                if len(s)>2:
                    break
                maxL=max(maxL,j-i+1)
        return maxL
    
fruits=[0,1,2,2,]
s=Solution()
print(s.totalFruit(fruits)) # 3

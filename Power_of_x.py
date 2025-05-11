class Solution:
    def getPower(self,x,n):
        if n==0:
            return 1
        if n%2==1:
            return x*self.getPower(x,n-1)
        return self.getPower(x*x,n//2)
    
    def myPow(self, x: float,n: int) -> float:
        if n<0:
            x=1/x
        n=abs(n)
        return self.getPower(x,n)
        
        
n = 49
x = 2
s=Solution()
res = s.myPow(x,n)
print(res)

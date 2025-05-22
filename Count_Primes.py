class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        prime=[1]*n
        for i in range(2,int(n**0.5)+1):
            if prime[i]==1:
                for j in range(i*i,n,i):
                    prime[j]=0
        c=0
        for i in range(2,n):
            if prime[i]==1:
                c+=1
        return c

        

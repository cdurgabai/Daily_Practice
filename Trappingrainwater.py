 #Trapping rain water
def watertrap(h):
    n=len(h)
    leftmax=[-1]*n
    leftmax[0]=h[0]
    for i in range(1,n):
        leftmax[i]=max(leftmax[i-1],h[i])
    rightmax=[-1]*n
    rightmax[n-1]=h[n-1]
    for i in range(n-2,-1,-1):
        rightmax[i]=max(rightmax[i+1],h[i])
    Min=[]
    for i in range(0,n):
        Min.append(min(rightmax[i],leftmax[i]))
    result=0
    for i in range(0,n):
        result+=Min[i]-h[i]
    return result
h=list(map(int,input().split()))
print(watertrap(h)) # 0 1 0 2 1 0 1 3 2 1 2 1 --> o/p: 6




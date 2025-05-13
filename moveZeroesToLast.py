# Code 2 Move zeroes to last --> TC=O(n)

a = list(map(int, input().split()))
res=[]

for num in a:
    if num!=0:
        res.append(num)
z_c=len(a)-len(res)

res+=[0]*z_c
print(res) #0 2 0 3 5 --> 2 3 5 0 0

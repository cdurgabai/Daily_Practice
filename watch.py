n=int(input())

for i in range(0,n):
     for j in range(0,i):
         print(" ",end=" ")
     for k in range((2*n)-((2*i)+1)):
         print("* ",end="")
     for j in range(0,i):
        print(" ",end=" ")
     print()
for i in range(1,n+1ch):
     for j in range(n-i):
         print(end="  ")
     for k in range((2*i)-1):
         print("* ",end="")
     print()

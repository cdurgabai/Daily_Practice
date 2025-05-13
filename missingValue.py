#Code 1 Missing Value in agiven list --> TC=O(n)
a = list(map(int, input().split()))
s=set(a)
i = 1
while i in s:
    i += 1
print(i) #1 2 3 4 --> 5

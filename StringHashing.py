s=input().strip()
p=11
hv=0
for i in range(len(s)):
  hv+=ord(s[i]*(p**(i+1))
print(hv)

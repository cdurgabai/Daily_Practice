def bs(s):
  b=0
  c=0
  
  for ch in s:
    if ch=='L':
      b+=1
    else:
      b-=1
    if b==0:
      c+=1
  return c

s=input()
print(bs(s))
  

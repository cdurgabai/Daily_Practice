# Longest or shortest length(Another concept)
# P2: The longest length subarray with sum k --> TC = O(n**2)

# More Optima Solution --> O(N)
arr=[2, 5, 1, 7, 10]
k=14
n=len(arr)
maxLen=0
lf=0
rt=0
Sum=0
while(rt<n): # O(N)
    Sum+=arr[rt] # Expand
    if Sum>k: # change while - if to optimize the code
        Sum-=arr[lf] # Shrink
        lf+=1
    maxLen=max(maxLen,rt-lf+1)
    rt+=1
print(maxLen) # 3

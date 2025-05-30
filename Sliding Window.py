# ? Sliding Window --> used in subarrays for optimization
# It is a constructive algorithm

# Code snippet
arr=[5,10,8]
n=len(arr)
for i in range(0,n):
    for j in range(i,n):
        print(arr[i:j+1])

"""
o/p: 
[5]
[5, 10]
[5, 10, 8]
[10]
[10, 8]
[8]
"""

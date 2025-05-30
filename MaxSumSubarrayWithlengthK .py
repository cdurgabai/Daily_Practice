# Constant Window --> One of the concept in Sliding window
# P1: Max Sum Subarray With length K --> TC = O(n**2)
# Optimal --> TC = O(n)
arr=[2,3,5,8,10,12,3,1]
k=4
n=len(arr)
maxSum=0
lf=0
rt=k-1
Sum=sum(arr[lf:rt+1])
maxSum=Sum
while rt<n-1:
    Sum-=arr[lf]
    lf+=1
    rt+=1
    Sum+=arr[rt]
    maxSum=max(maxSum,Sum)
print(maxSum) # 35

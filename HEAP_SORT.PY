def max_heap(arr,n,i):
    root=i
    lf=2*i+1
    rt=2*i+2
    if lf<n and arr[lf]>root:
        root=lf
    if rt<n and arr[rt]>root:
        root=rt
    if root!=i:
        arr[i],arr[root]=arr[root],arr[i]
        max_heap(arr,n,root)

def heapsort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        max_heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heap(arr,i,0)
    


arr = [10,1,6,4,11,13,2]
print(heapsort(arr))
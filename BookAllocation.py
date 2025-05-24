def findPages(arr: [int], n: int, m: int) -> int:
    def canWeAllocate(maxPages, arr):
        no_of_pages_Allocated = arr[0]
        students = 1
        for i in range(1, n):
            if arr[i] + no_of_pages_Allocated <= maxPages:
                no_of_pages_Allocated += arr[i]
            else:
                no_of_pages_Allocated = arr[i]
                students += 1
        return students
    if m>len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    res=-1

    while low<=high:
        maxPages=(low+high)//2
        if canWeAllocate(maxPages,arr)<=m:
            res=maxPages
            high=maxPages-1
        else:
            low=maxPages+1
    return res

arr=[12, 34, 67, 90]
n=4
m=2
print(findPages(arr,n,m)) # 113

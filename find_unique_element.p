def find_unique_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]

n = int(input())
arr = list(map(int, input().split()))
print(find_unique_element(arr))

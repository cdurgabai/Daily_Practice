def countTriangles(arr):
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            count += k - j - 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(countTriangles(arr))

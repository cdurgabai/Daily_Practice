from collections import defaultdict

def count_distinct_in_window(arr, k):
    freq = defaultdict(int)
    result = []
    for i in range(k):
        freq[arr[i]] += 1
    result.append(len(freq))
    for i in range(k, len(arr)):
        left = arr[i - k]
        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]
        freq[arr[i]] += 1
        result.append(len(freq))
Distinct Elements in Window    Distinct Elements in WindowrDistinct Elements in Windoweturn result

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    output = count_distinct_in_window(arr, K)
    print(*output)

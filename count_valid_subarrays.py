def count_valid_subarrays(arr):
    count = 0
    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 2] == arr[i + 1]:
            count += 1
    return count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(count_valid_subarrays(arr))

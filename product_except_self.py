def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = product_except_self(nums)
    print(result)

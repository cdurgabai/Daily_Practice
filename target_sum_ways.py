def target_sum_ways(nums, target):
    MOD = 10**9 + 7
    total_sum = sum(nums)

    # Edge cases
    if abs(target) > total_sum or (total_sum + target) % 2 != 0:
        return 0

    subset_sum = (total_sum + target) // 2

    # DP array
    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] = (dp[s] + dp[s - num]) % MOD

    return dp[subset_sum]


# User Input
n = int(input())
nums = list(map(int, input().split()))
target = int(input())

print(target_sum_ways(nums, target))

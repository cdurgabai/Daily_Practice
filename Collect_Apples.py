def collect_apples(maze):
    n = len(maze)
    m = len(maze[0])
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = maze[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + maze[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + maze[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + maze[i][j]
    return dp[-1][-1]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    print(collect_apples(maze))

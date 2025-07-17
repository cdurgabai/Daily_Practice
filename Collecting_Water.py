def watertrap(h):
    n = len(h)
    if n < 3:
        return 0

    leftmax = [0] * n
    rightmax = [0] * n

    leftmax[0] = h[0]
    for i in range(1, n):
        leftmax[i] = max(leftmax[i - 1], h[i])

    rightmax[-1] = h[-1]
    for i in range(n - 2, -1, -1):
        rightmax[i] = max(rightmax[i + 1], h[i])

    result = 0
    for i in range(n):
        result += max(0, min(leftmax[i], rightmax[i]) - h[i])

    return result

T = int(input())
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    print(watertrap(heights))

def generateSquare(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    i = n // 2
    j = n - 1
    for num in range(1, n * n + 1):
        mat[i][j] = num
        if num % n == 0:
            j -= 1
        else:
            i -= 1
            j += 1
        i = (i + n) % n
        j = (j + n) % n
    return mat

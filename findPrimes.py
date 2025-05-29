def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def sieve_method(n):
    is_prime = [1] * (n + 1)
    is_prime[0:2] = [0, 0]
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

def findPrimes(L, R):
    limit = isqrt(R) + 1
    base_primes = sieve_method(limit)
    result = []
    for num in range(max(L, 2), R + 1):
        root = isqrt(num)
        is_prime = 1
        for p in base_primes:
            if p > root:
                break
            if num % p == 0:
                is_prime = 0
                break
        if is_prime:
            result.append(num)
    return result

L, R = map(int, input().split())
primes = findPrimes(L, R)
print(" ".join(str(p) for p in primes))

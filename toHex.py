class Solution:
    def toHex(self, n):
        if n == 0:
            return "0"

        if n < 0:
            n += (2**32)
        res = []
        d = "0123456789abcdef"

        while n:

            res.append(d[n%16])

            n //= 16

        return "".join(res[::-1])

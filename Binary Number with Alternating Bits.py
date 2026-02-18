class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]  # The first 2 character is always 0b, so we slice it off.
        for i in range(1, len(binary)):
            if binary[i] == binary[i-1]:
                return False
        return True

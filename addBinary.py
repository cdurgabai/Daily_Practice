class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=int(a,2)+int(b,2)
        return bin(res)[2:]

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        return [[3,0],[2,1]][(lcm(p,q)//p)%2][(lcm(p,q)//q)%2]

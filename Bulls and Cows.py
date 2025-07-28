import string
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        n = len(secret)

        map1 = {}
        map2 = {}
        bulls = 0
        for i in range(n):
            a = secret[i]
            b = guess[i]
            if a == b:
                bulls += 1
            else:
                map1[a] = map1.get(a, 0) + 1
                map2[b] = map2.get(b, 0) + 1


        cows = 0
        #Count cows
        for i in string.digits:
            cows += min( map1.get(i,0) , map2.get(i,0))


        return f"{bulls}A{cows}B"

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        for a in range(len(words)):
            if words[a][0]!=s[a]:
                return False
        return True

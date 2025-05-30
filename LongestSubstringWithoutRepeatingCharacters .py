# Longest Substring Without Repeating Characters 
# Optimal
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxLen=0
        lf=0
        rt=0
        d={}
        maxLen=0
        while rt<n:
            if s[rt] in d:
                if d[s[rt]]>=lf:
                    lf=d[s[rt]]+1
            d[s[rt]]=rt
            maxLen=max(maxLen,rt-lf+1)
            rt+=1
        return maxLen
s = "adbzabcd"
sol=Solution()
print(sol.lengthOfLongestSubstring(s)) # 5   

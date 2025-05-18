class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        max_len = 0
        str_dictionary = {}
        for j in range(len(s)):
            if s[j] in str_dictionary and str_dictionary[s[j]] >= i:
                i = str_dictionary[s[j]] + 1
            str_dictionary[s[j]] = j
            max_len = max(max_len, j-i+1)
        return max_len

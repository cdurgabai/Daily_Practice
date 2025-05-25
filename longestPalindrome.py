from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = {}
        length = 0
        center = False

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        for word in list(freq):
            rev = word[::-1]
            if word == rev:
                pairs = freq[word] // 2
                length += pairs * 4
                freq[word] -= pairs * 2
                if not center and freq[word] > 0:
                    length += 2
                    center = True
            elif rev in freq:
                pairs = min(freq[word], freq[rev])
                length += pairs * 4
                freq[word] -= pairs
                freq[rev] -= pairs

        return length

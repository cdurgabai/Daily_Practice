class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        for n, i in enumerate(lst):
            lst[n] = i[::-1]
        return ' '.join(lst)
        

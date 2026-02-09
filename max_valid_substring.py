import math
from collections import defaultdict

def max_valid_substring(P, K):
    freq = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(P)):
        freq[P[right]] += 1

        while len(freq) > K:
            freq[P[left]] -= 1
            if freq[P[left]] == 0:
                del freq[P[left]]
            left += 1

        window_len = right - left + 1
        distinct = len(freq)
        non_distinct = window_len - distinct

        if math.ceil(window_len / 2) >= non_distinct:
            max_len = max(max_len, window_len)

    return max_len

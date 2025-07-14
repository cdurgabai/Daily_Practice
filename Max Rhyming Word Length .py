#Max Rhyming Word Length 
n = int(input())
words = []
for _ in range(n):
    words.append(input())
q = int(input())
for _ in range(q):
    query = list(input())
    max_len = 0
    curr_len = 0
    max_suff_len = 0
    for i in words:
        if(i[-1] == query[-1]):
            curr_len = len(i)
            k = -1
            while(abs(k) <= len(query)and abs(k) < len(i) and i[k] == query[k]):
                k-=1
            if abs(k) > max_suff_len or ((abs(k) == max_suff_len) and curr_len > max_len):
                max_len = curr_len
                max_suff_len = abs(k)
    print(max_len)

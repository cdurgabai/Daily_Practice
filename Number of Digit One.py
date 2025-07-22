class Solution:
    def countDigitOne(self, n: int) -> int:
        next_digit = 10
        current_digit = 1
        global_sum = 0

        #iterate through every digit/sequence
        while n >= current_digit:
            #number of "completed" 1-subsequences
            div = n // next_digit
            #last mod numbers can possibly contain last 1-subsequence
            mod = n % next_digit
            global_sum += div * current_digit
            #if this last 1-subsequence exists, it might be "completed" or not
            if mod >= current_digit:
                #before this last 1-subsequence, we have (currentDigit-1) zeroes.
                #(currentDigit-1) means 9, 99, 999,...
                #(currentDigit*2-1) means 19, 199, 1999...
                global_sum += min(mod, current_digit * 2 - 1) - (current_digit - 1)
            next_digit *= 10
            current_digit *= 10

        return global_sum

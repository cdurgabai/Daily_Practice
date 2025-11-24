class Solution:
    def minimumSum(self, num: int) -> int:
        max1, max2 = -1, -1
        min1, min2 = 10, 10

        while num > 0:
            temp = num % 10

            # Check for the max digits
            if max1 < temp:
                max2, max1 = max1, temp
            elif max2 < temp:
                max2 = temp

            # Check for the min digits
            if min1 > temp:
                min2, min1 = min1, temp
            elif min2 > temp:
                min2 = temp

            num //= 10

        return (min1 + min2) * 10 + max1 + max2

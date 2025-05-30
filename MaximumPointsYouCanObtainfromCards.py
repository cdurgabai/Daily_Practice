#Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints,k): #List[int], k: int) -> int:
        n = len(cardPoints)
        lf = 0
        rt = k - 1
        Sum = sum(cardPoints[lf:rt + 1])
        maxSum = Sum

        while rt >= 0:
            Sum -= cardPoints[rt]
            Sum += cardPoints[n - (k - rt)]
            maxSum = max(maxSum, Sum)
            rt -= 1

        return maxSum
cardPoints = [1,2,3,4,5,6,1]
k = 3
s=Solution()
print(s.maxScore(cardPoints,k)) # 12

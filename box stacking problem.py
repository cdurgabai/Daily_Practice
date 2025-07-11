class Solution:
    def __init__(self):
        self.dp = []
    
    def maxHeightRecur(self, i, boxes):
        if self.dp[i] != -1:
            return self.dp[i]

        max_height = boxes[i][2]
        for j in range(i + 1, len(boxes)):
            if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                max_height = max(max_height, boxes[i][2] + self.maxHeightRecur(j, boxes))

        self.dp[i] = max_height
        return self.dp[i]

    def maxHeight(self, height, width, length):
        n = len(height)
        boxes = []

        for i in range(n):
            a, b, c = height[i], width[i], length[i]
            # Only 3 unique orientations needed per box
            boxes.append([max(a, b), min(a, b), c])
            boxes.append([max(a, c), min(a, c), b])
            boxes.append([max(b, c), min(b, c), a])

        # Sort boxes by base area in descending order
        boxes.sort(key=lambda x: (x[0] * x[1]), reverse=True)

        self.dp = [-1] * len(boxes)
        max_stack_height = 0

        for i in range(len(boxes)):
            max_stack_height = max(max_stack_height, self.maxHeightRecur(i, boxes))

        return max_stack_height

height = [4, 1, 4, 10]
width = [6, 2, 5, 12]
length = [7, 3, 6, 32]
n = len(height)

print(findMaxHeight(height, width, length, n))


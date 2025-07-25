class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def base_area(self):
        return self.l * self.w

    def can_be_above(self, other):
        return self.l < other.l and self.w < other.w

def max_stack_height(boxes):
    rotations = []
    for l, w, h in boxes:
        for x, y, z in [(l, w, h), (w, h, l), (h, l, w)]:
            length = max(x, y)
            width = min(x, y)
            rotations.append(Box(length, width, z))
    rotations.sort(key=lambda box: box.base_area(), reverse=True)
    n = len(rotations)
    dp = [box.h for box in rotations]
    for i in range(n):
        for j in range(i):
            if rotations[i].can_be_above(rotations[j]):
                dp[i] = max(dp[i], dp[j] + rotations[i].h)
    return max(dp)

T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    W = list(map(int, input().split()))
    H = list(map(int, input().split()))
    boxes = list(zip(L, W, H))
    print(max_stack_height(boxes))

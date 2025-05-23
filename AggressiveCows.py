# AggressiveCows
def aggressiveCows(stalls, k):
    def canWePlace(minD, stalls, k):
        cow = stalls[0]
        placedC = 1
        for stall in range(1, len(stalls)):
            if stalls[stall] - cow >= minD:
                cow = stalls[stall]
                placedC += 1
            if placedC >= k:
                return True
        return placedC >= k

    stalls.sort()
    Min = stalls[0]
    Max = stalls[-1]
    
    if k == 2:
        return Max - Min
    
    left = 1
    right = Max - Min
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if canWePlace(mid, stalls, k):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

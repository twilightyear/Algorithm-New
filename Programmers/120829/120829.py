# 풀이 1
def solution(angle):
    return 1 if 0 < angle < 90 else 2 if angle == 90 else 4 if angle == 180 else 3

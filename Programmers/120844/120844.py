# 풀이 1
from collections import deque

def solution(numbers, direction):
    d = deque(numbers)
    if direction == "right":
        a = d.pop()
        d.appendleft(a)
        return list(d)
    else:
        a = d.popleft()
        d.append(a)
        return list(d)

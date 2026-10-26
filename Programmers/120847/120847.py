# 풀이 1
def solution(numbers):
    s = sorted(numbers)
    return s[-1]*s[-2]

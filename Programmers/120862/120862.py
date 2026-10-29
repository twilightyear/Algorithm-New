# 풀이 1
def solution(numbers):
    arr = sorted(numbers)
    return max(arr[-1]*arr[-2], arr[0]*arr[1])

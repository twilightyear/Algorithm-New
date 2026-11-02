# 풀이 1
def solution(array):
    result = 0
    for c in str(array):
        if c == '7':
            result += 1
    return result

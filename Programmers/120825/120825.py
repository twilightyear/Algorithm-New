# 풀이 1
def solution(my_string, n):
    result = ""
    for c in my_string:
        result += c*n
    return result

# 풀이 1
def solution(num, k):
    n = str(num)
    for i in range(len(n)):
        if n[i] == str(k):
            return i + 1
    return -1

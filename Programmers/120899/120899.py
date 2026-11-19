# 풀이 1
def solution(array):
    result = [array[0], 0]
    
    for i, num in enumerate(array):
        if num > result[0]:
            result[0] = num
            result[1] = i
    
    return result

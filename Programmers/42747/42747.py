# 풀이 1
def solution(citations):
    citations = sorted(citations, reverse=True)
    h = 0
    
    for i, n in enumerate(citations):
        if n >= i+1:
            h = i+1
        else:
            break
    
    return h

# 풀이 1
def solution(my_string):
    return sorted([ int(c) for c in my_string if c.isnumeric() == 1 ])

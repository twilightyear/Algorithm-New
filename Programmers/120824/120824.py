# 풀이 1
def solution(num_list):
    return [ sum([ 1 if n % 2 == 0 else 0 for n in num_list ]), sum([ 1 if n % 2 == 1 else 0 for n in num_list ])]

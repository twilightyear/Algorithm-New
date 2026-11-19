# 풀이 1
def solution(hp):
    g = int(hp/5)
    s = int((hp-g*5)/3)
    w = hp-g*5-s*3
    return g+s+w

# 풀이 1
def solution(my_string):
    result = ""
    
    for c in my_string:
        if c.isupper():
            result += c.lower()
        elif c.islower():
            result += c.upper()
    
    return result

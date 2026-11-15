# 풀이 1
def solution(my_string):
    vowels = ['a','e','i','o','u']
    result = ''
    for char in my_string:
        if char not in vowels:
            result += char
    return result

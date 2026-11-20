# 풀이 1
def solution(age):
    dictionary = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h",
        "8": "i",
        "9": "j"
    }
    return "".join(dictionary.get(c) for c in str(age))

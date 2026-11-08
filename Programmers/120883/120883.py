# 풀이 1
def solution(id_pw, db):
    return "login" if id_pw in db else ("fail" if id_pw[0] not in [row[0] for row in db] else "wrong pw")

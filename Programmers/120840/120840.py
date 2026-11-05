# 풀이 1
def solution(balls, share):
    
    def factorial(n):
        if n == 1 or n == 0:
            return 1
        return n * factorial(n-1)
    
    return int(factorial(balls)/(factorial(share)*factorial(balls-share)))

### [ Programmers ] 구슬을 나누는 경우의 수

### 🛠️ 풀이 접근 및 분석

  - **접근 1**
    - nCr 의 공식을 적용하여 n! / r!(n-r)! 의 공식을 그대로 사용했다. 팩토리얼을 구현하는 과정에서 재귀호출 스택 때문에 O(N) 의 공간복잡도가 발생하며, 마찬가지로 O(N) 의 시간복잡도가 발생한다.

### 📝 추후 개선점

  - 생각해보니, 공간복잡도를 O(N) 으로 만드는 주범인 재귀를 굳이 사용할 필요가 없다는 생각이 들었다. 즉, 단순 for 문을 사용하여 한번의 과정에서 전부 계산해버린다면, 시간복잡도는 그대로지만 공간복잡도를 O(1) 으로 개선할 수도 있다는 것을 파악했다. 이러한 점을 항상 염두해두어야겠다. 

### 💻 풀이 코드

```python
# 풀이 1
def solution(balls, share):
    
    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n-1)
    
    return int(factorial(balls)/(factorial(share)*factorial(balls-share)))
```

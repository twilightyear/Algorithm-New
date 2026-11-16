### [ Programmers ] 대문자와 소문자

### 🛠️ 풀이 접근 및 분석

  - **접근 1**
    - 대문자와 소문자를 판별할 수 있는 내장 함수인 isupper() 와 islower() 를 사용하여, my_string 의 값들을 순회하며 판별 및 변환한 추가를 구성했다. result 를 빈 문자열로 두고 추가를 한다면  최악의 경우 시간복잡도가 너무 높아질 수 있다는 점에 근거하여, 리스트에 append 를 하는 방식으로 O(1) 의 시간복잡도로 추가를 하고 최종적으로 join 을 사용하여 리스트를 하나의 문자열로 합친다면 최악의 경우 문자열의 길이 N 에 대하여 O(N) 의 시간복잡도와 공간복잡도를 가지게 된다.

### 📝 추후 개선점
  - 다른 사람들의 풀이를 찿아보니, swapcase() 라는 함수가 있다는 사실을 알았다. 이를 통하여 보다 효율적이고 간결하게 코드를 구성할 수 있었던 것이다... 항상 이런것을 볼때마다 배워가는 것 같다.

### 💻 풀이 코드

```python
# 풀이 1
def solution(my_string):
    result = []
    
    for c in my_string:
        if c.isupper():
            result.append(c.lower())
        elif c.islower():
            result.append(c.upper())
    
    return "".join(result)
```

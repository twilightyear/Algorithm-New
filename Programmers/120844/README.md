### [ Programmers ] 배열 회전시키기

### 🛠️ 풀이 접근 및 분석

  - **접근 1**
    - 배열의 뒷부분을 앞으로 추가하거나, 앞부분을 뒤로 추가하는 단일 연산이 필요하기에, deque 을 채택했다. 이렇게 한다면 O(1) 의 시간복잡도가 발생하나, list 로 별로로 변환하는 과정에서 O(N) 의 시간복잡도와 공간복잡도가 발생하게 된다.

### 📝 추후 개선점
  - 다른 사람들의 풀이를 살펴보니, 슬라이싱으로 한줄로 풀이한 것을 보았다. 두가지 경우 모두, 직접 가장 끝 부분을 슬라이싱하고, 나머지 부분도 슬라이싱하여 합차는 것이다. 결국 O(N) 의 시간복잡도와 공간복잡도를 가지는 것은 동일하지만, 내부적으로 슬라이싱은 C 레벨에서 동작한다는 특성상, 접근 1번보다 빠르게 동작할 것으로 기대할 수 있다.

### 💻 풀이 코드

```python
# 풀이 1
from collections import deque

def solution(numbers, direction):
    d = deque(numbers)
    if direction == "right":
        a = d.pop()
        d.appendleft(a)
        return list(d)
    else:
        a = d.popleft()
        d.append(a)
        return list(d)
```

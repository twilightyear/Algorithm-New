### [ Programmers ] H-Index

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
 - 역정렬을 통하여 배열을 제자리에 정렬해둔후, 앞에서부터 순서대로 항목과 인덱스 순서를 enumerate 를 통하여 가장 큰 n 부터 n >=i+1 를 만족하는 n 의 최대값을 구하는 방식으로 진행한다면, O(NlogN) 의 시간복잡도와, O(1) 의 공간복잡도를 가지게 할 수 있다.

### 📝 추후 개선점
  - 생각해보니, h 값을 사용하지 않고도 단순 구조를 개선해서 처음 n >= i+1 을 불만족하는 경우, 즉 n < i+1 인 경우에 i 값을 반환하게 한다면 굳이 h 라는 변수를 관리하지 않고도 코드를 구성할 수 있었겠다라는 생각을 했다. 물론 시간복잡도와 공간복잡도적인 부분에서의 수식적인 개선은 없겠지만, 이러한 사소한 구조 개선 또한 나중에 유용하게 사용할 사고 방식일 수 있다.

### 💻 풀이 코드

```python
# 풀이 1
def solution(citations):
    citations = sorted(citations, reverse=True)
    h = 0
    
    for i, n in enumerate(citations):
        if n >= i+1:
            h = i+1
        else:
            break
    
    return h
```

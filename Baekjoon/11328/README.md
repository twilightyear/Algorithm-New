### [ Baekjoon ] 11328 : Strfry

### 🛠️ 풀이 접근 및 분석

-   **접근 1**
 - 주어진 문자열을 정렬하고 같은지 확인하는 방식으로 비교가 가능하다. 여기서 반복 횟수 M, 문자열의 길이 N 에 대하여 O(M*NlogN) 의 시간복잡도가 발생하며, O(N) 의 공간복잡도가 발생한다.

### 📝 추후 개선점
 - 문자 등장 횟수를 사용하여 코드를 개선할 방향이 존재한다. 미리 사전정의한 알파벳들에 대한 배열을 만들어두고 문자 등장 횟수를 업데이트 및 비교, 루프마다 초기화를 한다면 O(M * N) 의 시간복잡도와 O(1) 의 공간복잡도를 가지도록 개선할 수 있다.

### 💻 풀이 코드

```python
# 풀이 1
c = int(input())

for _ in range(c):
  arr = list(map(str, input().split()))
  if sorted(arr[0]) == sorted(arr[1]):
    print("Possible")
  else:
    print("Impossible")
```

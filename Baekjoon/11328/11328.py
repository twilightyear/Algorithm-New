# 풀이 1
c = int(input())

for _ in range(c):
  arr = list(map(str, input().split()))
  if sorted(arr[0]) == sorted(arr[1]):
    print("Possible")
  else:
    print("Impossible")

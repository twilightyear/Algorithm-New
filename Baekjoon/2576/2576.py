# 풀이 1
arr = []

for _ in range(7):
  arr.append(int(input()))

arr = [n for n in arr if n % 2 != 0]

if len(arr) == 0:
  print(-1)
else:
  print(sum(arr))
  print(min(arr))

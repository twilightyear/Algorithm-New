# 풀이 1
result = []
for i in range(20):
  result.append(i+1)

for _ in range(10):
  arr = list(map(int, input().split()))
  a, b = arr[0], arr[1]
  x = result[:a-1]
  y = result[a-1:b]
  z = result[b:]

  y.reverse()
  x.extend(y)
  x.extend(z)
  result = x

for n in result:
  print(n, end=" ")

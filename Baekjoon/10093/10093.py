# 풀이 1
arr = list(map(int,input().split()))
a = min(arr[0], arr[1])
b = max(arr[0], arr[1])

if a == b:
  print(0)
else:
  print(b - a - 1)
  
for i in range(a+1, b):
  print(i, end = " ")

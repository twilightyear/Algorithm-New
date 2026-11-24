# 풀이 1
for _ in range(3):
  arr = list(map(int, input().split()))
  val = sum(arr)

  if val == 4:
    print("E")
  elif val == 3:
    print("A")
  elif val == 2:
    print("B")
  elif val == 1:
    print("C")
  elif val == 0:
    print("D")

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  elif b % a == 0 and a != b:
    print('factor')
  elif a % b == 0 and a != b:
    print('multiple')
  else:
    print('neither')
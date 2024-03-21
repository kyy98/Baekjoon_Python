a = int(input())

for i in range(a):
  A, B = map(int, input().split())
  print('Case #'+str(i+1)+':',A, '+', B, '=', A+B)
A, B = map(int, input().split())
C = int(input())

if C >= 60:
    A += C // 60
    B += C % 60
else:
    B += C

if B >= 60:
    B %= 60
    A += 1

A %= 24

print(A, B)
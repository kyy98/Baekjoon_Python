import sys
input = sys.stdin.readline

t = int(input())
cnt0 = [0]*41
cnt1 = [0]*41

cnt0[0], cnt1[0] = 1,0
cnt0[1], cnt1[1] = 0, 1

for i in range(2,41):
    cnt0[i] = cnt0[i-2]+cnt0[i-1]
    cnt1[i] = cnt1[i-2]+cnt1[i-1]

for _ in range(t):
    n = int(input())
    print(cnt0[n], cnt1[n])
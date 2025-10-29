N = int(input())
ls_1 = list(map(int, input().split()))
ls_2 = list(map(int, input().split()))

ls_1.sort()
ls_2.sort(reverse=True)
ans = 0

for i in range(N):
    ans+=ls_1[i]*ls_2[i]
print(ans)
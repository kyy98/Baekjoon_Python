N, S = map(int, input().split())
data = list(map(int, input().split()))
lst = []

end = 0
interval_sum = 0

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += data[end]
        end += 1
    if interval_sum >= S:
        lst.append(end-start)
    interval_sum -= data[start]
if lst == []:
    print(0)
else:
    print(min(lst))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    arr_2.sort()

    def bin_s(target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr_2[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start

    result = 0
    for t in arr_1:
        result += bin_s(t, 0, b - 1)

    print(result)

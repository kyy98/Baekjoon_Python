import collections


while True:
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break

    ls = []
    answer = []
    for _ in range(n):
        a = list(map(int, input().split()))
        ls+=a

    dic = dict(collections.Counter(ls))
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    largest = dic[0]

    for i in range(1, len(dic)):
        if dic[i][1] < largest[1]:
            largest = dic[i]
            break

    for j in range(dic.index(largest), len(dic)):
        if dic[j][1] == largest[1]:
            answer.append(dic[j][0])
    answer.sort()
    print(*answer)
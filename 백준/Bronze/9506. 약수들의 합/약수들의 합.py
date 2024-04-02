while True:
    num = int(input())
    if num == -1:
        break
    lst = [i for i in range(1, num) if num % i == 0]
    if num == sum(lst):
        print(num, '=', end=' ')
        for k in range(len(lst)-1):
            print(lst[k], '+', end=' ')
        print(lst[-1])
    else:
        print(num, 'is NOT perfect.')
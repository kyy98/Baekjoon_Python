x, y, w, h = map(int, input().split())

a, b, c, d = x, y, w-x, h-y
lst = [a,b,c,d]
print(min(lst))
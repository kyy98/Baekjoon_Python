N = int(input())
a = list(map(int, input().split()))
M = max(a)
new = [i/M*100 for i in a]
print(sum(new)/len(new))
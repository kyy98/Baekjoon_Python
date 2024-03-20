A = input()
B = input()

for i in reversed(range(len(B))):
    print(int(B[i])*int(A))
print(int(A)*int(B))    
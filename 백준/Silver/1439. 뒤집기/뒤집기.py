s = input()
cnt_a = 0
cnt_b = 0

if s[0] == '0':
    cnt_a+=1
else:
    cnt_b+=1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            cnt_a+=1
        else:
            cnt_b+=1
            
print(min(cnt_a, cnt_b))
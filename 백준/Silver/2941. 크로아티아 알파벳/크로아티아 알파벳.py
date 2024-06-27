w = input()
cnt = len(w)

for i in range(len(w)-1):
    if 'c=' == w[i:i+2]:
        cnt-=1
    elif 'c-' == w[i:i+2]:
        cnt-=1
    elif 'd-' == w[i:i+2]:
        cnt-=1
    elif 'lj' == w[i:i+2]:
        cnt-=1
    elif 'nj' == w[i:i+2]:
        cnt-=1
    elif 's=' == w[i:i+2]:
        cnt-=1
    elif 'z=' == w[i:i+2]:
        if 'dz=' == w[i-1:i+2]:
            cnt -= 2
        else:
            cnt-=1


print(cnt)
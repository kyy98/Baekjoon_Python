from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = 0
    dict = Counter(tangerine)
    ls = []
    for i, num in dict.items():
        ls.append(num)
    ls_s = sorted(ls, reverse=True)
    for n in ls_s:
        answer+=n
        cnt+=1
        if answer >= k:
            break
    return cnt
 
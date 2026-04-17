# # 예외 케이스: 여벌 체육복이 있지만 본인 것도 잃은 경우
# # reserve에 있는 사람 중복 counting 조심
# # 정렬

def solution(n, lost, reserve):
    r_s = set(reserve)-set(lost)
    l_s = set(lost)-set(reserve)
    
    for i in r_s:
        if i-1 in l_s:
            l_s.remove(i-1)
        elif i+1 in l_s:
            l_s.remove(i+1)
    return n-(len(l_s))
   
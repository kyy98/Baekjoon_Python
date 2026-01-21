# # 예외 케이스: 여벌 체육복이 있지만 본인 것도 잃은 경우
# # reserve에 있는 사람 중복 counting 조심
# # 정렬

def solution(n, lost, reserve):
    reserve_del = set(reserve)-set(lost)
    lost_del = set(lost)-set(reserve)
    
    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
    
    return n-len(lost_del)
        
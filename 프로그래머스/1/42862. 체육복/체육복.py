# # 예외 케이스: 여벌 체육복이 있지만 본인 것도 잃은 경우
# # reserve에 있는 사람 중복 counting 조심
# # 정렬
# def solution(n, lost, reserve):
#     lost = sorted([i for i in lost if i not in reserve])
#     reserve = sorted([i for i in reserve if i not in lost])
    
#     for i in range(len(reserve)):      
#         if reserve[i]-1 in lost:
#             lost.remove(reserve[i]-1)
#         elif reserve[i]+1 in lost:
#             lost.remove(reserve[i]+1) 
        
#     return n-len(lost)

def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1) :
        # 도난 당한 학생이다
        if i in lost :
            # 그런데 내가 여벌 체육복이 있다
            if i in reserve :
                answer +=1 
            # 내가 여벌 체육복이 없어서 빌려야 한다
            else :
                for j in range(i-1,i+2):
                    # 인접한 번호의 친구가 갖고 있는데, 얘도 빌려줄 여력이 된다
                    if j in reserve and j not in lost :
                        answer += 1
                        reserve.remove(j)
                        break

        # 도난 당하지 않았다
        else :
            answer += 1

    return answer
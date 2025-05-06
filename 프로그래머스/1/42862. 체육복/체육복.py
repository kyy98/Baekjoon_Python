# def solution(n, lost, reserve):
#     lost = set(lost) - set(reserve)
#     reserve = set(reserve) - set(lost)

#     for r in sorted(reserve):
#         if r - 1 in lost:
#             lost.remove(r - 1)
#         elif r + 1 in lost:
#             lost.remove(r + 1)

#     return n - len(lost)
def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    total = [1] * (n+2)
    total[0] = 0
    total[-1] = 0
    
    for i in lost:
        total[i] -= 1
        
    for i in reserve:
        total[i] += 1
    
    for i in lost:
        if total[i] == 0 and total[i-1] == 2:
            total[i-1] = 1
            total[i] = 1
        if total[i] == 0 and total[i+1]==2:
            total[i+1] = 1
            total[i] = 1
            
    print(total) # 확인용
    
    for i in total:
        if i > 0:
            answer += 1
    
    return answer

# 연속된 번호의 학생에게만 빌려줄수있음
# 최대한 많은 학생이 체육복을 가지고있어야함
# 앞으로 줄지 뒤로줄지 고민해야함

# 뒷번호에게 줄때, 그 뒷번호의뒤에 2인사람이 없으면 그냥 주기

def solution(name):
    answer = 0
    n = len(name)
    
    # 1. 알파벳(상하 이동)
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    # 2. 커서 이동(좌우)
    move = n - 1  # 기본: 오른쪽으로 쭉 가는 경우
    
    for i in range(n):
        next = i + 1
        
        # 연속된 A 구간 찾기
        while next < n and name[next] == 'A':
            next += 1
        
        # 2가지 케이스 비교
        move = min(move,
                   2 * i + (n - next),        # 갔다가 돌아오기
                   i + 2 * (n - next))        # 뒤부터 갔다가 오기
    
    return answer + move
def solution(n, lost, reserve):
    # 정렬
    lost.sort()
	
    # 여벌 체육복을 가져온 학생도 도난당했을 수 있기 때문에 실질적으로 빌려줄 수 있는 학생만 걸러줌
    r = [i for i in reserve if i not in lost]
    l = [j for j in lost if j not in reserve]
    r = sorted(r)
    l = sorted(l)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in r:
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)

    return n-len(l)
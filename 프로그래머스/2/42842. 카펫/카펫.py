def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if 2*(yellow_x)+2*(yellow_y)+4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                break
        answer = sorted(answer)
    return answer
            
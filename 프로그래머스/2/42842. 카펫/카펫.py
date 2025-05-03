def solution(brown, yellow):
    yellow_x = 0
    yellow_y = 0
    answer = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            yellow_x = yellow//i
            yellow_y = i
            if 2*yellow_x+2*yellow_y+4 == brown+yellow-(yellow_x*yellow_y):
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                break
    return answer
    
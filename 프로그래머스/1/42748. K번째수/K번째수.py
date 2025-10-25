def solution(array, commands):
    answer = []
    for c in commands:
        array_2 = array[c[0]-1:c[1]]
        array_3 = sorted(array_2)
        idx = array_3[c[2]-1]
        answer.append(idx)
    return answer
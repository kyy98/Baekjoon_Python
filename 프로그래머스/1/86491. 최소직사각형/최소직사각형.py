sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    ls_1 = []
    ls_2 = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    for i in sizes:
        ls_1.append(i[0])
        ls_2.append(i[1])
        
    return max(ls_1)*max(ls_2)
solution(sizes)
        
            
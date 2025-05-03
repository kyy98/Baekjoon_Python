def solution(numbers, target):
    leaves = [0]            
    cnt = 0
    
    for num in numbers:
        temp = []
        for leave in leaves:
            temp.append(leave+num)
            temp.append(leave-num)
        leaves = temp
        
    for leave in leaves:
        if leave == target:
            cnt+=1
    return cnt
            
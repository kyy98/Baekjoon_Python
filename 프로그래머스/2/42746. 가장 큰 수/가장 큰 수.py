def solution(numbers):
    answer = ''
    ls = []
    for n in numbers:
        ls.append(str(n))
    ls.sort(key = lambda x: x*3, reverse=True)
    if ls[0] == '0':
        answer+='0'
    else:
        for i in ls:
            answer += i
    return answer
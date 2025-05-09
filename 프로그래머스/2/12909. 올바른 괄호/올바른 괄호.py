

def solution(s):
    ls = []
    for i in s:
        if i == '(':
            ls.append(i)
        else:
            if ls == []:     # 스택이 비어 있으면 닫는 괄호가 많다는 뜻
                return False
            ls.pop()         # 마지막 여는 괄호 제거 (pop(0) ❌ pop() ✅)
    if ls != []:             # 여는 괄호가 남아 있음 → 짝이 안 맞음
        return False
    return True

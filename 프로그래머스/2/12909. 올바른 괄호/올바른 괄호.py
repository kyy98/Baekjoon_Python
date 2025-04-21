s = '()()'

def solution(s):
    ls = []
    for i in s:
        if i == '(':
            ls.append(i)
        else:
            if ls != []:
                ls.pop(0)

    if ls != []:
        return True
    return False
solution(s)           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     ls = []
#     for i in s:
#         if i == '(':
#             ls.append(i)
#         else:
#             if ls == []:
#                 return False
#             else:
#                 ls.pop(0)
#     if ls != []:
#         return False
#     return True
#     solution(s)

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

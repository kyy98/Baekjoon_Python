def solution(s):
    ls = s.split()
    
    ls_u = [i.capitalize() for i in ls]
    
    return ' '.join(i for i in ls_u)
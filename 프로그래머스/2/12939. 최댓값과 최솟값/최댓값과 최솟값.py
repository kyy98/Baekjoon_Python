def solution(s):
    ls = s.split()
    ls_int = [int(i) for i in ls]
    ls_int.sort()
    ls_int.sort()
    return str(ls_int[0])+" "+str(ls_int[-1])
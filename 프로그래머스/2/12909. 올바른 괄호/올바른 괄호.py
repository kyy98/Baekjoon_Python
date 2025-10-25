def solution(s):
    ls = []
    if s[0] == ')':
        return False
    else:
        try:
            for i in range(len(s)):
                if s[i] == '(':
                    ls.append(s[i])
                else:
                    ls.pop()
            if len(ls) > 0:
                return False

            else:
                return True
        except IndexError:
            return False
            
        
def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return len(stack)==0
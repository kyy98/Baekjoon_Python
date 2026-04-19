def solution(s):
    stack = [s[0]]
    if len(s) == 1:
        return False
    else:
        for char in s[1:]:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
    
  
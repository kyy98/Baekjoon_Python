def solution(number, k):
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k>0:
            stack.pop()
            k-=1
        stack.append(num)
    
    if k!=0:
        stack = stack[:-k]
    return ''.join(stack)

        
    



# from itertools import combinations
# def solution(number, k):
#     ls_1 = []
#     ls_2 = []
#     for i in number:
#         ls_1.append(i)
#     for p in combinations(ls_1, len(number)-k):
#         if p[0] == max(ls_1):
#             ls_2.append(''.join(p))
#     ls_2.sort()
        
#     return max(ls_2)
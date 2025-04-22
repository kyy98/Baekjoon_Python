citations = [3, 0, 6, 1, 5]

# def solution(citations):
#     h_idx = 0
#     cit = sorted(citations, reverse=True)
#     for i, j in enumerate(cit):
#         if j <= i+1:
#             return j
#     return len(citations)-1
            
    
# solution(citations)            
            
1
2
3
4
5
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer



            
        
            
            
            
            
        
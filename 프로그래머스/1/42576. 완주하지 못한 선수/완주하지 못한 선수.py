participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

# def solution(participant, completion):
    # dict_1 = dict(zip(participant, [participant.count(i) for i in participant]))

#     for i in participant:
#         if i not in completion:
#             return i
#         else:
#             if participant.count(i) != completion.count(i):
#                 return i
            

# solution(participant, completion)

def solution(participant, completion):
    hash_dict = dict()
    p_sum = 0
    for p in participant:
        hash_dict[hash(p)] = p
        p_sum+=hash(p)
    for c in completion:
        p_sum-=hash(c)
    return hash_dict[p_sum]
solution(participant, completion)     
    
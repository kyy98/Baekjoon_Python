from collections import Counter
def solution(participant, completion):
    dict_1 = Counter(participant)
    dict_2 = Counter(completion)
#     dict_1 = {} 
#     dict_2 = {}
#     for i in range(len(participant)):
#         name_p = participant[i]
#         count_p = participant.count(name_p)
#         dict_1[name_p] = count_p  
#     for j in range(len(completion)):
#         name_c = completion[j]
#         count_c = completion.count(name_c)
#         dict_2[name_c] = count_c
  
    for k in dict_1.keys():
        if k not in dict_2.keys():
            return k
        else:
            if dict_2[k] != dict_1[k]:
                return k
    